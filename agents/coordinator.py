from .planner_agent import plan_task
from .researcher_agent import research
from .coder_agent import write_code
from .executor_agent import execute
from .critic_agent import critique
from .improver_agent import improve
from .memory_agent import save_lesson

def run_goal(goal: str) -> str:
    print("Planning...")
    plan = plan_task(goal)
    print(plan)

    print("Researching...")
    knowledge = research(goal)
    print("Knowledge:", knowledge)

    print("Coding...")
    code = write_code(goal)
    print(code)

    print("Executing...")
    result = execute(code)
    print("Result:", result)

    print("Critiquing...")
    feedback = critique(goal, result)
    print(feedback)

    lesson = improve(feedback)
    print("Lesson learned:", lesson)

    save_lesson(goal, lesson)

    return result
