import contextlib
import sys

from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(__file__)


def drink_recommendation_test():
    # reset the knowledge engine
    engine.reset()

    # activate drink_recommender_rules.krb
    engine.activate('drink_recommender_rules')

    print("doing proof")

    try:
        print("Here are some categories of drinks you might like:")
        with engine.prove_goal('drink_recommender_rules.drinks($drinks)') as gen:
            for index, (vars, plan) in enumerate(gen):
                category = vars['drinks'][0]
                also = "also " if index > 0 else ""
                print(f"You can {also}take {category}")
                print(f"Here are some of {category} you should try:")
                for index, item in enumerate(vars['drinks'][1:]):
                    print(f"\n{index}. {item}")

    except Exception:
        print("in exception")
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")
