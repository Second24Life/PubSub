from abc import ABCMeta, abstractmethod

# Абстрактный класс для издателя
class Publisher():
	__metaclass__=ABCMeta
	
	def add_news(self, channel, news):
		channel.publish(news)

# Абстрактный класс для канала событий	
# метод publish добавляет новых наблюдателей в комнату
# метод subscribe сообщает наблюдателям о новом событии
class EventChannel():
	__metaclass__=ABCMeta

	def subscribe(self, nameRoom='CommonChat', subscriber):
		self.rooms[nameRoome].append(subscriber)

	def publish(self, nameRoom='CommonChat', message):
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
# метод add_news вызывает метод notify из абстрактного класса, чтобы сообщить о новости 
class Newspaper(Publisher):

	def __init__(self, name, yearOfCreate):
		self.name = name
		self.yearOfCreate = yearOfCreate

class ChatRoom(EventChannel):

	def __init__(self, name):
		self.name = name
		self.rooms = []

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
chatRoomIT.subscribe(maksim)
chatRoomCar.subscribe(maksim)
chatRoomIT.subscribe(igor)

# Газета добавляет новую новость и сообщает о ней подписчикам
newspaper.add_news(chatRoomIT, 'Good news came to our city ...')
newspaper.add_news(chatRoomCar, 'Gasoline has again risen in price.')

# Газета добавляет новость о отписке своего подпичсика
newspaper.add_news(chatRoomIT, 'We lost the Igor.')