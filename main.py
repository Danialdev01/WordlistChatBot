import re
import jawapan_panjang as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    #^ kira berapa kali perkataan ada dalam satu prkataan 
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    #^ kira kemungkinan perkataan dalam satu ayat untuk check jawapan yang paling tepat 
    percentage = float(message_certainty) / float(len(recognised_words))

    #^ check perkataan dalm string 
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    #^ perkataan yang mesti ada 
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    #^ tambah perkataan kepada dictionary 
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #^ Respon -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'hai', 'hei'], single_response=True)
    response('waalaikum salam', ['salam', 'aslm', 'assalamualaikum', 'asalamualaikum', 'asalam', 'assalamualaikum warahmatullah'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'irfan', 'danial'], required_words=[ 'i', 'love', 'danial'])
    response('Aku takde umur', ['kau', 'berapa', 'ini', 'berapa', 'umur'], required_words=[ 'kau', 'umur', 'berapa'])
    response('goodnight awak , tido jangan lupa ingat saya', ['selamat','malam','awak'], required_words=['selamat','malam', 'awak'])


    #^ Respon(jawapan) yang panjang 
    response(long.R_ADVICE, ['bagi', 'nasihat'], required_words=['bagi', 'nasihat'])
    response(long.R_EATING, ['apa', 'kau', 'makan'], required_words=['kau', 'makan'])
    response(long.R_TANYA, ['saya', 'nak', 'tanya', 'kenapa'], required_words=[ 'nak', 'tanya'])
    response(long.R_DANIALINFO, ['danial', 'siapakah', 'siapa'], required_words=['siapa', 'danial'])
    response(long.R_BOTINFO, ['kau', 'apa', 'siapa', 'ni'], required_words=['siapa', 'kau'])
    response(long.R_BOTJAWAP, ['tengah', 'buat', 'kau', 'apa'], required_words=['buat', 'kau'])
    response(long.R_BOTJAWAP, ['tengah', 'buat', 'tu', 'apa'], required_words=['buat', 'apa'])
    response(long.R_FUNTIONBOT, ['ni', 'kau', 'fungsi', 'apa'], required_words=['fungsi', 'kau'])
    response(long.R_DANIALBUAT, ['danial', 'tengah', 'buat', 'apa'], required_words=['buat', 'danial', 'tengah'])
    response(long.R_SIAPABOT, ['kau', 'ini', 'siapa', 'sebenarnya'], required_words=['kau', 'apa'])
    response(long.R_HOWBOT, ['bagaimana', 'danial', 'buat', 'kau', 'macam', 'mana'], required_words=['macam', 'danial', 'buat', 'kau'])
    response(long.R_BETULKA, ['betulkah', 'betul', 'ke', 'danial', 'program', 'buat', 'kau'], required_words=['danial', 'buat', 'kau'])
    response(long.R_CANTIKKAH, ['kenapa', 'kau', 'cantik', 'sangat'], required_words=['awak', 'cantik'])
    


    

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    #^ untuk dapat info penuh 
   # print(highest_prob_list)
    print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


#^ guna untuk dapat respon (filter untuk respon)
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


#!( tulisan kepada suara (text to speech))(PLS betulkan)
#cakap = 
#friend.say(cakap)
#friend.runAndWait()

#^ untuk test sistem
while True:
    print('Bot: ' + get_response(input('You: ')))

