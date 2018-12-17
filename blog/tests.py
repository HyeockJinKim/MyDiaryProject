from django.test import TestCase


# Create your tests here.
from django.utils import timezone

from blog.models import Diary, WithMe, Subject, Location


class BlogModelTest(TestCase):
    def setUp(self):
        with_me = WithMe.objects.create(
            name='누군가',
            description='내가 아는 누군가'
        )
        subject = Subject.objects.create(
            name='팀프로젝트',
            description='어떤 과목 팀 프로젝트'
        )
        location = Location.objects.create(
            name='CNU',
            description='학교'
        )
        diary = Diary.objects.create(
            title='팀프로젝트 진행상황',
            subject=subject,
            post='팀원의 업무 분배와 인터페이스를 구현하였다.',
            location=location,
        )
        diary.with_me.add(with_me)

    def test_diary(self):
        saved_models = Diary.objects.count()
        self.assertEqual(saved_models, 1)
        today = timezone.localdate()
        diary = Diary.objects.filter(
            date=today
        )

        self.assertIsNotNone(diary)
        self.assertEqual(diary.count(), 1)
        self.assertEqual(diary[0].date, timezone.localdate())
