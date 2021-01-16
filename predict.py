intents = {"intents": [
  {"tag": "chào bạn hê hê",
    "patterns": ["Chào bạn", "xin chào", "Có ai ở đó không", "Chúc một ngày tốt lành"],
    "responses": ["chào, cám ơn vì ghé thăm", "rất vui vì gặp lại bạn", "chào, tôi có thể giúp gì nào"],
    "context_set": ""
  },
  {"tag": "goodbye",
  "patterns": ["Tạm biệt", "Gặp lại bạn sau", "hẹn gặp lại"],
  "responses": ["hẹn gặp lai sau, cảm ơn đã ghé thăm", "Chúc một ngày tốt lành", "Tạm biệt! Hãy quay lại sớm."]
  },
  {"tag": "question1",
    "patterns": ["Coronavirus là gì?"],
    "responses": ["Vi rút Corona là một họ vi rút lớn có thể gây bệnh cho động vật hoặc người. Ở người, một số coronavirus được biết là gây ra các bệnh nhiễm trùng đường hô hấp, từ cảm lạnh thông thường đến các bệnh nặng hơn như Hội chứng Hô hấp Trung Đông (MERS) và Hội chứng Hô hấp cấp tính nặng (SARS. Coronavirus được phát hiện gần đây nhất gây ra bệnh coronavirus COVID-19."]
  },
  {"tag": "question2",
    "patterns": ["COVID-19 lây lan như thế nào?"],
    "responses": ["COVID-19 có nhiều khả năng lây lan từ người này sang người khác thông qua: 1. tiếp xúc với một người trong khi họ đang lây nhiễm hoặc trong 24 giờ trước khi các triệu chứng của họ xuất hiện 2. tiếp xúc với một người đã được xác nhận nhiễm trùng ho hoặc hắt hơi 3. chạm vào các đồ vật hoặc bề mặt (chẳng hạn như tay nắm cửa hoặc bàn) bị ô nhiễm khi ho hoặc hắt hơi từ một người đã được xác nhận nhiễm trùng và sau đó chạm vào miệng hoặc mặt của bạn."]
  },
  {"tag": "question3",
    "patterns": ["Tôi có thể rời khỏi nhà không?"],
    "responses": ["Tất cả mọi người được yêu cầu ở nhà trừ khi thực sự cần thiết phải ra ngoài."]
  },
  {"tag": "question4",
    "patterns": ["Tôi có nên xét nghiệm COVID-19 không?"],
    "responses": ["Bác sĩ sẽ cho bạn biết liệu bạn có nên đi xét nghiệm hay không. Họ sẽ sắp xếp cho bài kiểm tra."]
  },
  {"tag": "question5",
    "patterns": ["Tôi có nên đeo khẩu trang không?"],
    "responses": ["Bạn không cần phải đeo khẩu trang nếu bạn khỏe mạnh. Để biết thêm thông tin về việc sử dụng khẩu trang phẫu thuật, hãy truy cập trang này trên trang web Sức khỏe"]
  },
  {"tag": "question6",
    "patterns": ["Tôi có nên đưa con tôi ra khỏi nhà trẻ hoặc trường học không?"],
    "responses": ["Trường học và nhà trẻ bị đóng cửa cho đến khi có lệnh."]
  },
  {"tag": "question7",
    "patterns": ["Còn phương tiện giao thông công cộng như máy bay, xe buýt, xe lửa đi chung và taxi?"],
    "responses": ["Chính phủ khuyến nghị người sử dụng lao động phải bố trí làm việc linh hoạt để giảm thiểu số lượng người sử dụng phương tiện giao thông công cộng cùng một lúc. Các dịch vụ đường dài có nguy cơ lây nhiễm cao hơn và cần được xem xét lại vào lúc này."]
  },
  {"tag": "question8",
    "patterns": ["Chính phủ đang làm gì để ngăn chặn sự lây lan của COVID-19?"],
    "responses": ["Chính phủ đang tuân thủ các hướng dẫn của WHO một cách cẩn thận và mọi cấp độ của máy móc y tế công cộng đều phù hợp với nó. Bộ Y tế cập nhật liên tục về số ca bệnh và đưa ra hướng dẫn cho các bác sĩ và bệnh viện về việc cách ly và điều trị bệnh nhân mắc bệnh. Chính phủ đã ngăn chặn việc nhập cảnh của những người từ các quốc gia bị ảnh hưởng bởi căn bệnh này bằng cách hủy bỏ thị thực. Những người nghi mắc bệnh đang được xét nghiệm. Các cơ sở kiểm dịch đã được triển khai ở nhiều địa điểm. Một cơ chế lý tưởng để kiểm tra bất kỳ ai nghi ngờ họ mắc bệnh nên được đưa ra nhưng điều này vẫn chưa xảy ra."]
  },
  {"tag": "question9",
    "patterns": ["Nhiễm trùng này sẽ tồn tại hay biến mất? Thời tiết ấm hơn có giúp ngăn chặn vi rút lây lan không? Nó sẽ xuất hiện trở lại khi thời tiết lạnh hơn trở lại?"],
    "responses": ["Điều này đặc biệt khó đoán. Một số bệnh do vi rút (ví dụ như bệnh cúm) phần lớn là theo mùa và có xu hướng lây lan dễ dàng hơn vào mùa đông hơn là trong cái nóng của mùa hè. Hiện tại, chúng tôi không biết liệu COVID-19 có thuộc loại này hay không. Nó có thể biến mất hoàn toàn sau mùa hè hoặc có lẽ là kịch bản khả dĩ hơn - nó có thể xuất hiện trở lại trong đợt thứ hai. Chúng tôi chỉ đơn giản là chưa biết."]
  },
  {"tag": "question10",
    "patterns": ["Có vaccine ngừa hoặc loại thuốc tôi có thể dùng nếu bị nhiễm bệnh không?"],
    "responses": ["Vẫn chưa mặc dù nhiều phòng thí nghiệm trên thế giới đang nghiên cứu về vấn đề này. Có một số ứng cử viên vắc xin đang được phát triển và một số loại thuốc hiện có cho các bệnh khác đang được thử nghiệm trên bệnh nhân COVID-19 để xem liệu chúng có hoạt động hay không. Việc tạo ra một loại vắc xin an toàn có thể mất thời gian tối đa là một hoặc hai năm."]
  },
  {"tag": "question11",
    "patterns": ["COVID-19 là gì"],
    "responses": ["COVID-19 là bệnh truyền nhiễm do virus corona được phát hiện gần đây nhất gây ra. Loại virus và căn bệnh mới này chưa được biết đến trước khi bùng phát ở Vũ Hán, Trung Quốc vào tháng 12 năm 2019."]
  },
  {"tag": "question12",
    "patterns": ["Các triệu chứng của COVID-19 là gì", "Các biểu hiện của COVID-19 là gì"],
    "responses": ["Các triệu chứng phổ biến nhất của COVID-19 là sốt mệt mỏi và ho khan. Một số bệnh nhân có thể bị đau nhức và nghẹt mũi, chảy nước mũi, đau họng hoặc tiêu chảy. Các triệu chứng này thường nhẹ và bắt đầu dần dần Một số người bị nhiễm bệnh nhưng không phát triển bất kỳ triệu chứng nào và không cảm thấy không khỏe. Hầu hết mọi người (khoảng 80%) đều khỏi bệnh mà không cần điều trị đặc biệt. Cứ 6 người nhiễm COVID-19 thì có 1 người bị bệnh nặng và khó thở"]
  },
  {"tag": "question13",
    "patterns": ["Vi rút gây ra COVID-19 có thể lây truyền qua không khí không?"],
    "responses": ["Các nghiên cứu cho đến nay cho thấy vi rút gây ra COVID-19 chủ yếu lây truyền qua tiếp xúc với các giọt đường hô hấp hơn là qua không khí. Xem câu trả lời trước về COVID-19 lây lan như thế nào?"]
  },
  {"tag": "question14",
    "patterns": ["CoVID-19 có thể bị lây nhiễm từ một người không có triệu chứng không?"],
    "responses": ["Con đường lây lan chính của bệnh là qua các giọt đường hô hấp do người đang ho tống ra. Nguy cơ nhiễm COVID-19 từ người không có triệu chứng là rất thấp, tuy nhiên nhiều người bị COVID-19 chỉ gặp các triệu chứng nhẹ."]
  },
  {"tag": "question15",
    "patterns": ["Tôi có thể nhiễm COVID-19 từ phân của người mắc bệnh không?"],
    "responses": ["Nguy cơ nhiễm COVID-19 từ phân của một người bị nhiễm bệnh dường như là thấp Trong khi các điều tra ban đầu cho thấy vi rút có thể có trong phân trong một số trường hợp lây lan qua con đường này không phải là đặc điểm chính của đợt bùng phát. Nghiên cứu đang tiếp tục về các cách thức COVID -19 được lan truyền và sẽ tiếp tục chia sẻ những phát hiện mới"]
  },
  {"tag": "question16",
    "patterns": ["Tôi có thể làm gì để bảo vệ bản thân và ngăn ngừa bệnh lây lan"],
    "responses": ["1. Thường xuyên và kỹ lưỡng vệ sinh tay của bạn bằng dung dịch xoa tay có cồn \ n Giữ khoảng cách ít nhất 1 mét (3 feet) giữa bạn và người đang ho hoặc hắt hơi \ nTránh chạm vào mắt mũi và miệng \ n Đảm bảo bạn và những người xung quanh bạn tuân theo vệ sinh hô hấp tốt. Điều này có nghĩa là bạn phải che miệng và mũi bằng khuỷu tay cong hoặc khăn giấy khi ho hoặc hắt hơi \ n Hãy về nhà nếu bạn cảm thấy không khỏe \ n Luôn cập nhật các điểm phát sóng COVID-19 mới nhất (các thành phố hoặc khu vực địa phương nơi COVID-19 đang lan rộng )."]
  },
  {"tag": "question17",
    "patterns": ["Tôi có khả năng mắc phải COVID-19 như thế nào?"],
    "responses": ["Rủi ro phụ thuộc vào vị trí của bạn - và cụ thể hơn là liệu có bùng phát COVID-19 ở đó hay không."]
  },
  {"tag": "question18",
    "patterns": ["Tôi có nên lo lắng về COVID-19 không?"],
    "responses": ["Bệnh tật do nhiễm COVID-19 thường nhẹ, đặc biệt đối với trẻ em và thanh niên"]
  },
  {"tag": "question19",
    "patterns": ["Ai có nguy cơ mắc bệnh nặng"],
    "responses": ["Trong khi chúng tôi vẫn đang tìm hiểu về cách COVID-2019 ảnh hưởng đến những người lớn tuổi và những người có bệnh từ trước (chẳng hạn như bệnh cao huyết áp, bệnh tim, ung thư phổi hoặc tiểu đường) dường như phát triển bệnh nghiêm trọng thường xuyên hơn những người khác."]
  },
  {"tag": "question20",
    "patterns": ["Thuốc kháng sinh có hiệu quả trong việc ngăn ngừa hoặc điều trị COVID-19 không?"],
    "responses": ["Không. Thuốc kháng sinh không hoạt động chống lại vi rút mà chỉ có tác dụng đối với các bệnh nhiễm trùng do vi khuẩn"]
  },
  {"tag": "question21",
    "patterns": ["Có bất kỳ loại thuốc hoặc liệu pháp nào có thể ngăn ngừa hoặc chữa khỏi COVID-19 không"],
    "responses": ["Mặc dù một số phương pháp điều trị tại nhà hoặc cổ truyền phương Tây có thể mang lại sự thoải mái và giảm bớt các triệu chứng của COVID-19, nhưng không có bằng chứng nào cho thấy y học hiện tại có thể ngăn ngừa hoặc chữa khỏi bệnh"]
  },
  {"tag": "question22",
    "patterns": ["Có thuốc chủng ngừa hoặc điều trị COVID-19 không"],
    "responses": ["Chưa Tuy nhiên những người bị ảnh hưởng nên được chăm sóc để giảm các triệu chứng."]
  },
  {"tag": "question23",
    "patterns": ["COVID-19 có giống với SARS không?"],
    "responses": ["Không. Vi-rút gây ra COVID-19 và vi-rút gây bùng phát Hội chứng hô hấp cấp tính nghiêm trọng (SARS) vào năm 2003 có liên quan đến nhau về mặt di truyền"]
  },
  {"tag": "question24",
    "patterns": ["Thời gian ủ bệnh của COVID-19 là bao lâu?"],
    "responses": ["'Thời kỳ ủ bệnh' có nghĩa là khoảng thời gian từ khi nhiễm vi rút đến khi bắt đầu có các triệu chứng của bệnh Hầu hết các ước tính về thời gian ủ bệnh của COVID-19 là từ 1-14 ngày, phổ biến nhất là khoảng năm ngày. Các ước tính này sẽ được cập nhật khi có nhiều dữ liệu hơn."]
  },
  {"tag": "question25",
    "patterns": ["Con người có thể bị nhiễm COVID-19 từ nguồn động vật không?"],
    "responses": ["Để bảo vệ bản thân như khi đến chợ động vật sống tránh tiếp xúc trực tiếp với động vật và các bề mặt tiếp xúc với động vật. Đảm bảo thực hành tốt an toàn thực phẩm mọi lúc"]
  },
  {"tag": "question26",
    "patterns": ["Tôi có thể bắt COVID-19 từ thú cưng của mình không?"],
    "responses": ["Mặc dù đã có một trường hợp chó bị nhiễm bệnh ở Hồng Kông cho đến nay, nhưng không có bằng chứng cho thấy chó mèo hoặc bất kỳ vật nuôi nào có thể truyền COVID-19 COVID-19 chủ yếu lây lan qua các giọt được tạo ra khi người bị nhiễm bệnh ho hắt hơi hoặc nói."]
  },
  {"tag": "question27",
    "patterns": ["Virus tồn tại trên bề mặt bao lâu?"],
    "responses": ["Không rõ vi rút gây ra COVID-19 tồn tại trên bề mặt bao lâu nhưng nó có vẻ hoạt động giống như các vi rút corona khác Các nghiên cứu cho thấy vi rút corona (bao gồm thông tin sơ bộ về vi rút COVID-19) có thể tồn tại trên bề mặt trong vài giờ hoặc lên đến vài ngày"]
  },
  {"tag": "question28",
    "patterns": ["Có an toàn để nhận một gói hàng từ bất kỳ khu vực nào mà COVID-19 đã được báo cáo không?"],
    "responses": ["Đúng. Khả năng một người bị nhiễm lây nhiễm sang hàng hóa thương mại là thấp và nguy cơ nhiễm vi rút gây ra COVID-19 từ một gói hàng đã được vận chuyển và tiếp xúc với các điều kiện và nhiệt độ khác nhau cũng thấp."]
  },
  {"tag": "question29",
    "patterns": ["Có điều gì tôi không nên làm không?"],
  },
  {"tag": "question30",
    "patterns": ["Tác nhân gây bệnh Covid-19 là gì?", "nguyên nhân gây bệnh covid-19"],
    "responses": ["Tác nhân gây bệnh Covid-19 là một chủng virus Corona.Chủng virus gây bệnh Covid-19 khác hẳn với các chủng virusCorona đã biết trước đó nên đã được đặt tên là “virusCorona mới” (Novel Coronavirrus - viết tắt là nCoV). Trong danh pháp khoa học, tên chủng virus mới còn có thêm thông tin về năm phát hiện, do vậy tên đầy đủ của chủng virus Corona mới này là “2019 Novel Coronavirus” viết tắt hay ký hiệu là “2019-nCoV”"]
  },
  {"tag": "question31",
    "patterns": ["Virus Covid-19 tồn tại bao lâu trong môi trường tự nhiên?", "Virus Covid-19 duy trì bao lâu trong môi trường tự nhiên?"],
    "responses": ["Trong môi trường tự nhiên, virus chỉ tồn tại nguyên dạng và không nhân lên, do vậy thời gian sống của virus trong môitrường tự nhiên là thời gian tồn tại của một thế hệ virus. Thời gian này là bao lâu sẽ phụ thuộc vào bản chất của virus và các điều kiện tự nhiên. Thông thường, ở nhiệt độ lạnh virus sẽ tồn tại lâu hơn, nhất là nhiệt độ lạnh âm sâu; các yếu tố khác như độ ẩm, chất liệu bề mặt (đất, gỗ, sắt…) cũng ảnh hưởng đến thời gian tồn tại của virus; đặc biệt ánh sáng mặt trời có tác dụng tiêu diệt virus rất hiệu quả. "]
  },
  {"tag": "question32",
    "patterns": ["Thế nào là tự cách ly?", "tự cách ly là gì"],
    "responses": ["Tự cách ly là việc tự cá nhân bị nghi ngờ mắc bệnh truyền nhiễm nhưng chưa có triệu chứng bị bệnh hoặc đã xét nghiệm âm tính với mầm bệnh nhưng nghi ngờ chưa thực sự hết khả năng lây nhiễm chủ động cách ly bản thân nhằm hạn chế sự lây truyền bệnh."]
  },
  {"tag": "question33",
    "patterns": ["Tại sao tôi cần đeo khẩu trang?", "Đeo khẩu trang có tác dụng gì"],
    "responses": ["Khẩu trang là một rào chắn đơn giản giúp ngăn các giọt bắn từ đường hô hấp của quý vị tiếp xúc với người khác. Các nghiên cứu chỉ ra rằng đeo khẩu trang che mũi và miệng giúp làm giảm các giọt bắn ra ngoài. Quý vị nên đeo khẩu trang, ngay cả khi quý vị không cảm thấy bị bệnh."]
  },
  {"tag": "numberCovidCase",
    "patterns": ["có bao nhiêu trường hợp covid 19 ở việt nam ?", "tình hình covid 19 ở viêt nam", "số ca covid"],
    "responses": ["tình hình covid 19 ở việt nam: "]
  },
  {"tag": "phoneNumber",
    "patterns": ["Đường dây nóng tư vấn COVID-19", "Số điện thoại liên hệ tư vấn"],
    "responses": ["ĐƯỜNG DÂY NÓNG BỘ Y TẾ: 1900.9095, Email: duongdaynong@moh.gov.vn"]
  }
]}


# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import regex
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

from underthesea import word_tokenize

import numpy as np
import tflearn
import tensorflow as tf
import random

import requests

import COVID19Py



import pickle
data = pickle.load( open( "./models/training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']


net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
covid19 = COVID19Py.COVID19()


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)

    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

# load model
model.load('./models/model.tflearn')
context = {}

ERROR_THRESHOLD = 0.25
def classify(sentence):
    results = model.predict([bow(sentence, words)])[0]
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    print(return_list)
    return return_list

def response(sentence, show_details=False):
    return (sentence)
#     results = classify(sentence)
#     if results:
#         while results:
#             for i in intents['intents']:
#                 if i['tag'] == results[0][0]:
#                   if results[0][0] in "numberCovidCase":
#                     NumberComfirmed = " Số người mắc bệnh: " + str((covid19.getLocationByCountryCode("VN"))[0]["latest"]["confirmed"])
#                     NumberDeath = ", Số người chết: " + str((covid19.getLocationByCountryCode("VN"))[0]["latest"]["deaths"])
#                     print((random.choice(i['responses'])) + NumberComfirmed + NumberDeath)
#                     return ((random.choice(i['responses'])) + NumberComfirmed + NumberDeath)
#                   else:
#                     return 'hi'
                  
#             results.pop(0)
