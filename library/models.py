from django.db import models
from django.utils import timezone
from datetime import timedelta

# 1. 書籍資料表
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="書名")
    author = models.CharField(max_length=100, verbose_name="作者")
    isbn = models.CharField(max_length=20, unique=True, verbose_name="ISBN")
    is_available = models.BooleanField(default=True, verbose_name="是否可借閱")

    def __str__(self):
        return self.title

# 2. 借閱紀錄資料表（滿足借還功能、期限與逾期偵測）
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="借閱書籍")
    user_name = models.CharField(max_length=100, verbose_name="借閱人姓名")
    borrow_date = models.DateTimeField(auto_now_add=True, verbose_name="借閱時間")
    return_date = models.DateTimeField(null=True, blank=True, verbose_name="歸還時間")
    
    # 預設借閱期限為 14 天
    due_date = models.DateTimeField(verbose_name="應還時間")

    def save(self, *args, **kwargs):
        # 如果是第一次建立紀錄，自動計算 14 天后的應還時間
        if not self.id and not self.due_date:
            self.due_date = timezone.now() + timedelta(days=14)
        super().add_to_class if hasattr(super(), 'add_to_class') else super().save(*args, **kwargs)

    @property
    def is_overdue(self):
        """檢查是否借閱逾期"""
        # 如果還沒歸還，且目前時間已經超過應還時間，就是逾期
        if not self.return_date and timezone.now() > self.due_date:
            return True
        return False

    def __str__(self):
        return f"{self.user_name} 借閱 {self.book.title}"