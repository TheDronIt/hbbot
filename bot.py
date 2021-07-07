import vk_api
from datetime import datetime, timedelta
import time
from multiprocessing import Process

print("Bot launched")

token = "" #VK KateMobile token

vk = vk_api.VkApi(token=token).get_api()

owner_vk_id = 000000000 #Change to your vk id 

def Timer():
	while 1:

		#Today info
		current_datetime = datetime.now()
		day_today = current_datetime.day
		month_today = current_datetime.month

		now_hour = current_datetime.hour
		now_minute = current_datetime.minute



		
		if now_hour == 7 and now_minute == 0:

			#Update info about HB
			owner_firends_info_not_processed = vk.friends.get(user_id=owner_vk_id, order="name", fields="bdate", name_case="nom")['items']
			owner_firends_info = []
			#print(owner_firends_info_not_processed)


			#Deleted users and none HB date filter
			for i in range(0, len(owner_firends_info_not_processed)):
				if owner_firends_info_not_processed[i]['first_name'] != 'DELETED':
					try:
						if owner_firends_info_not_processed[i]['bdate']:
							first_name = owner_firends_info_not_processed[i]['first_name']
							last_name = owner_firends_info_not_processed[i]['last_name']
							id = owner_firends_info_not_processed[i]['id']
							bdate = owner_firends_info_not_processed[i]['bdate']
							owner_firends_info.append({'first_name':first_name, 'last_name':last_name, 'id':id, 'bdate':bdate})	
					except:
						pass


			#Send message
			for i in range(0, len(owner_firends_info)):
				hb_info = owner_firends_info[i]['bdate'].split('.')
				if int(hb_info[0]) == day_today and int(hb_info[1]) == month_today:
					try:
						#vk.messages.send(user_id=owner_vk_id, message="Поздравить с др "+str(owner_firends_info[i]['first_name']), random_id=0)
						vk.messages.send(user_id=owner_firends_info[i]['id'], message="Поздравляю тебя с Днем Рождения🎁🎉. 💙\nЖелаю✨ светлой🍁, яркой⚡, бодрой🍬 и бешено веселой😃 жизни🌍...Ни о чем не жалеть.✊ Четко верить👼 в свой успех😌, и идти👣 по жизни🌍 с высоко поднятой головой💃, смотря только вперед💁. Всегда🙈 добиваться поставленных целей☝. Чтоб вся🙌 жизнь🌍 протекала как праздник.🎁🎂 Никогда🙅 не плыть за течением.💦 Любить❤ только тех, кто на это заслуживает💑. Чтоб все проблемы😱, с годами🌍 превращались✨ в приобретенный опыт🙏, который ты потом передашь💁 детям и внукам🙇👶👵. Желаю✨ каждый день🙉 просыпаться😴 с улыбкой😌 на лице. Радоваться😃 всем мелочам😃, и не воспринимать всерьез проблемы🔥🙌. Любить❤, и знать, что любят тебя!!!💎💍", random_id=0)
					except: 
						print("Message for "+str(owner_firends_info[i]['first_name'])+" "+str(owner_firends_info[i]['last_name'])+" ("+str(owner_firends_info[i]['id'])+") was not sent. (privacy settings)")
					congratulated = open('congratulated.txt', 'a')
					congratulated.write(", "+str(owner_firends_info[i]['id']))
					congratulated.close()
		




		#Отчистка поздравленных каждый месяц
		if day_today == 1:
			if now_hour == 1 and now_minute == 0:
				congratulated = open('congratulated.txt', 'w')
				congratulated.write("0")
				congratulated.close()
				print("File congratulated was cleaned")


		time.sleep(60)
		

if __name__ == '__main__':
    Process(target=Timer).start()
