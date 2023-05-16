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
        # print("Here are some drinks you might like:")
        with engine.prove_goal('drink_recommender_rules.drinks($drinks)') as gen:
            for vars, plan in gen:
                print(vars['drinks'], vars)
        #         print("Here are some of the questions you should practice:")
        #         for index, item in enumerate(vars['links']):
        #             # STUDENTS: you will need to edit this line
        #             print(f"\n{index + 1}. {item}")

    except Exception:
        print("in exception")
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")
