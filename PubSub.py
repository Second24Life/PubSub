from abc import ABCMeta, abstractmethod

# Абстрактный класс для издателя
class Publisher():
	__metaclass__=ABCMeta
	
	def add_news(self, channel, nameRoom, news):
		channel.publish(nameRoom, news)

# Абстрактный класс для канала событий	
# метод publish добавляет новых наблюдателей в комнату
# метод subscribe сообщает наблюдателям о новом событии
class EventChannel():
	__metaclass__=ABCMeta

	def subscribe(self, nameRoom, subscriber):
		if nameRoom in self.rooms:
			self.rooms[nameRoom].append(subscriber)

	def publish(self, nameRoom, message):
		if nameRoom in self.rooms:
			for subscriber in self.rooms[nameRoom]:
				subscriber.update(message + '\nP.s. {}\n{}'.format(nameRoom, '-'*11))
		

# Абстрактный класс для подписчика
# имеет метод update, который необходимо обязательно переопределить в наследуемых классах
# метод update выполняет какое-либо действие после того как наблюдаемый объект сообщить об событии
class Subscriber():
	__metaclass__=ABCMeta

	@abstractmethod
	def update(self, message):
		pass

# Класс газеты и немного минимум информации
class Newspaper(Publisher):

	def __init__(self, name, yearOfCreate):
		self.name = name
		self.yearOfCreate = yearOfCreate

class ChatRoom(EventChannel):
	nameRoom = 'CommonChat'
	rooms = {}

	def __init__(self, nameRoom):
		self.nameRoom = nameRoom
		self.rooms[nameRoom] = []

# Класс горожанина и немного информации о нем
# метод update переопределен
class Citizen(Subscriber):

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def update(self, message):
		print('{} learned the: {}'.format(self.name, message))

# Создаем объект класса Newspaper
newspaper = Newspaper('City', 1980)
# Создаем объекты класса ChatRoom
chatRoomIT = ChatRoom('ITNews')
chatRoomCar = ChatRoom('CarNews')
# Создаем объекты класса Citizen
maksim = Citizen('Max', 20)
igor = Citizen('Igor', 20)
# Подписываем созданных горожан на газету
chatRoomIT.subscribe(chatRoomIT.nameRoom, maksim)
chatRoomCar.subscribe(chatRoomCar.nameRoom, maksim)
chatRoomIT.subscribe(chatRoomIT.nameRoom, igor)

# Газета добавляет новую новость и сообщает о ней подписчикам
newspaper.add_news(chatRoomIT, 'new', 'Good news came to our city ...')
newspaper.add_news(chatRoomCar, chatRoomCar.nameRoom, 'Gasoline has again risen in price.')

newspaper.add_news(chatRoomIT, chatRoomIT.nameRoom, 'We lost the Igor.')