from abc import ABCMeta, abstractmethod

# Абстрактный класс для издателя
class Publisher():
	__metaclass__=ABCMeta
	
	def add_news(self, channel, news):
		channel.notify(news)

# Абстрактный класс для канала событий	
# метод register добавляет новых наблюдателей
# метод detach отцепляет наблюдателя от наблюдаемого объекта
# метод notify сообщает наблюдателям о новом событии
class EventChannel():
	__metaclass__=ABCMeta
	name = 'CommonChat'

	def register(self, subscriber):
		self.subscribers.append(subscriber)

	def detach(self, subscriber):
		if subscriber in self.subscribers:
			self.subscribers.remove(subscriber)

	def notify(self, message):
		for subscriber in self.subscribers:
			subscriber.update(message + '\nP.s. {}\n{}'.format(self.name, '-'*11))

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
		self.subscribers = []

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
chatRoomIT.register(maksim)
chatRoomCar.register(maksim)
chatRoomIT.register(igor)


# Газета добавляет новую новость и сообщает о ней подписчикам
newspaper.add_news(chatRoomIT, 'Good news came to our city ...')
newspaper.add_news(chatRoomCar, 'Gasoline has again risen in price.')
# Один из горожан решил отписаться от газеты
chatRoom.detach(igor)

# Газета добавляет новость о отписке своего подпичсика
newspaper.add_news(chatRoomIT, 'We lost the Igor.')