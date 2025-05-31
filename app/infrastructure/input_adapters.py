# Infrastructure - Input adapter
def get_user_input(prompt):
    return input(prompt)


def merge_gui_state_with_user_input(user_input, gui_state):

    merged_dic_data = gui_state.copy()
    for key in user_input.keys():
        merged_dic_data[key] = user_input.get(key)
    return merged_dic_data


def pair_gui_state_with_questions(states, questions):

    paired_dic = {}
    if len(states) == len(questions):
        for element in range(len(states)):
            paired_dic[questions[element]] = states[element]
    return paired_dic
