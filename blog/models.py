from django.conf import settings 
from django.db import models
from django.utils import timezone #他のファイルから何かをちょこっとずつ追加する行


# Create your models here.

class Post(models.Model): ##モデルの名前で、他の名前をつけることもできます
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #これは他のモデルへのリンク
    title=models.CharField(max_length=200) #文字数が制限されたテキストを定義するフィールド
    text=models.TextField() #これは制限無しの長いテキスト用
    created_date = models.DateTimeField(default=timezone.now) #日付と時間のフィールド
    published_date = models.DateTimeField(blank=True,null=True)

    def published (self):
        self.published_date=timezone.now()
        self.save()

    def __str__ (self):
        return self.title #__str__() を呼ぶと、ポストのタイトルのテキスト（string）が返ってきます。

        #class キーワードに続く行ではメソッドをインデント