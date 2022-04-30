from django.db import models

class Topic(models.Model):
    """内容的主题"""
    text = models.CharField(max_length=200)
    data_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """某个主题的具体内容"""
    topic = models.ForeignKey(
        Topic, 
        models.SET_NULL,
        blank=True,
        null=True,
    )
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else: 
            return self.text
