from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app.main import bp
from app.models import Problem, Attempt
from app import db

@bp.route('/')
@bp.route('/index')
def index():
    return redirect(url_for('main.dashboard'))

@bp.route('/dashboard')
def dashboard():
    recent_problems = Problem.query.order_by(Problem.created_at.desc()).limit(5).all()
    recent_attempts = Attempt.query.order_by(Attempt.timestamp.desc()).limit(10).all()
    return render_template('dashboard.html', title='대시보드',
                         recent_problems=recent_problems,
                         recent_attempts=recent_attempts)

@bp.route('/practice')
def practice():
    problems = Problem.query.all()
    return render_template('practice.html', title='학습하기', problems=problems)

@bp.route('/generate_problem', methods=['POST'])
def generate_problem():
    category = request.form.get('category')
    difficulty = request.form.get('difficulty')
    
    # 예시 문제 생성 (실제로는 AI 모델을 사용하여 생성해야 함)
    sample_problems = {
        'grammar': {
            'beginner': {
                'question': '다음 문장의 빈칸에 알맞은 것은? \n나는 어제 학교___ 갔다.',
                'options': ['에', '를', '가', '은'],
                'correct_answer': '0',
                'explanation': '장소를 나타내는 조사 "에"가 올바른 답입니다.'
            },
            'intermediate': {
                'question': '다음 중 현재진행형이 올바르게 사용된 문장은?',
                'options': [
                    'I am go to school.',
                    'I going to school.',
                    'I am going to school.',
                    'I is going to school.'
                ],
                'correct_answer': '2',
                'explanation': 'am/is/are + going 형태가 현재진행형의 올바른 형태입니다.'
            }
        },
        'vocabulary': {
            'beginner': {
                'question': '"사과"의 영어 단어로 올바른 것은?',
                'options': ['banana', 'apple', 'orange', 'grape'],
                'correct_answer': '1',
                'explanation': 'apple이 "사과"의 올바른 영어 단어입니다.'
            }
        }
    }

    problem_template = sample_problems.get(category, {}).get(difficulty, {
        'question': '기본 문제',
        'options': ['A', 'B', 'C', 'D'],
        'correct_answer': '0',
        'explanation': '기본 설명'
    })

    problem = Problem(
        question=problem_template['question'],
        options=problem_template['options'],
        correct_answer=problem_template['correct_answer'],
        explanation=problem_template['explanation'],
        difficulty=difficulty,
        category=category
    )
    db.session.add(problem)
    db.session.commit()

    flash('새로운 문제가 생성되었습니다!', 'success')
    return redirect(url_for('main.problem', id=problem.id))

@bp.route('/problem/<int:id>', methods=['GET', 'POST'])
def problem(id):
    problem = Problem.query.get_or_404(id)
    if request.method == 'POST':
        answer = request.form.get('answer')
        if not answer:
            flash('답을 선택해주세요', 'error')
            return redirect(url_for('main.problem', id=id))
            
        is_correct = answer == problem.correct_answer
        attempt = Attempt(
            problem_id=id,
            answer=answer,
            is_correct=is_correct,
            user_id=current_user.id if not current_user.is_anonymous else None
        )
        db.session.add(attempt)
        db.session.commit()
        
        flash('정답입니다!' if is_correct else '틀렸습니다. 다시 시도해보세요!',
              'success' if is_correct else 'error')
        return redirect(url_for('main.problem', id=id))
        
    return render_template('problem.html', title='문제 풀기', problem=problem)