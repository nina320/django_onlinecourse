# 可以把這個程式想成是一個空的datebase
# 我們可以在這隻程式當中去建立一個一個的table
# 設定好後，再執行某個功能，我們的資料庫db.sqlite3就會依照我們在這裡所規劃的樣子搭建出來

# 我們之後對models.py所做的修改，都會被記錄到migrations那個資料夾裡，方便追蹤
# 亦利於把資料庫的版本回到之前的 (版本控制)

from django.db import models
from django.db.models import CharField, DateField, ForeignKey, IntegerField
from django.contrib.auth.models import User


BALANCE_TYPE = ((u'收入',u'收入'),(u"支出", u"支出"))
# ((key, value), (key, value))

# Create your models here.
# 把它寫成python的類別，一個類別就是一個table
class Category(models.Model):   # 這裡我們要繼承 models.Model
	# columns 就是類別當中的變數  , 參見 https://docs.djangoproject.com/en/2.2/ref/models/fields/	
	category = CharField(max_length = 20)
	user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

	def __str__(self):  # 定義當我們今天要print這個物件時，它會以啥樣的名稱顯示
		return self.category     # 在這指定用 category做為它的指定名稱


class Record(models.Model):
	date = DateField()
	description = CharField(max_length = 300)
	category = ForeignKey(Category, on_delete = models.SET_NULL, null = True)  # 欄位名稱要和相關聯的欄位名稱一樣
	# 括號內輸入關聯欄位所在的table名稱
	# 後面另加兩個參數，目前先不解釋，後面的單元會說明
	cash = IntegerField()
	balance_type = CharField(max_length = 2, choices = BALANCE_TYPE)  # 收入或支出都只要兩個字
	user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

	def __str__(self):  # 定義當我們今天要print這個物件時，它會以啥樣的名稱顯示
		return self.description     # 在這指定用 description做為它的指定名稱

	# 可參考 https://docs.djangoproject.com/en/2.2/topics/db/queries/