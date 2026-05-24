from rest_framework import serializers
from .models import Book, BorrowRecord

# 1. 書籍資料轉換器
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# 2. 借閱紀錄轉換器 (包含應還日期與逾期判斷)
class BorrowRecordSerializer(serializers.ModelSerializer):
    # 把 models 裡面的 property 欄位也拉進來轉成 JSON 丟給前端
    is_overdue = serializers.ReadOnlyField()
    book_title = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'book_title', 'user_name', 'borrow_date', 'due_date', 'return_date', 'is_overdue']