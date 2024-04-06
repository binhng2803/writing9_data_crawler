from writing9.band import Band
from writing9.essay import Essay


with Essay() as bot:
    bot.land_page()
    # res = bot.get_question()
    # res = bot.get_topic()
    # res = bot.get_essay()
    # res = bot.get_feedback()
    # res = bot.get_num_linking_words()
    # res = bot.get_num_word_repetition()
    # res = bot.get_num_grammar_mistakes()
    # res = bot.get_num_paragraphs_and_words()
    # res = bot.get_detail_score()
    res = bot.essay_details()
    # res = bot.get_overall_band()
    print(res)
    # res = bot.pull_all_essay_on_page()
    # print(res)
    print('exiting ...')

