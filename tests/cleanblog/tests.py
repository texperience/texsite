# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist

from ..tests import TexsiteTestCase
from texsite.cleanblog.models import CleanBlogArticleIndexPage, CleanBlogArticlePage


class CleanBlogTestCase(TexsiteTestCase):
    def setUp(self):
        super(CleanBlogTestCase, self).setUp()

        try:
            self.article_index_page = CleanBlogArticleIndexPage.objects.get(pk=2)
            self.article_page = CleanBlogArticlePage.objects.get(pk=3)
            self.article_page_two = CleanBlogArticlePage.objects.get(pk=4)
        except ObjectDoesNotExist:
            pass

        self.article_index_page_response = self.client.get('/article-index-page/')
        self.article_page_response = self.client.get('/article-index-page/article-page/')


class CleanBlogStandaloneArticleIndexPageTest(CleanBlogTestCase):
    fixtures = ['site.json', 'cleanblogarticleindex.json']

    def test_article_index_empty_rendered(self):
        self.assertInHTML('<p>No entries found</p>', str(self.article_index_page_response.content))

    def test_article_index_articles_property_returns_zero_child_pages(self):
        self.assertEqual(len(self.article_index_page.articles), 0)

    def test_article_index_has_articles_paginator_in_context(self):
        self.assertEqual(self.article_index_page_response.status_code, 200)
        self.assertEqual(self.article_index_page_response.context['articles'].has_other_pages(), False)

    def test_article_index_with_wrong_page_number_succeeds(self):
        article_index_page_response = self.client.get('/article-index-page/?page=0')
        self.assertEqual(article_index_page_response.status_code, 200)


class CleanBlogArticlePageTest(CleanBlogTestCase):
    fixtures = ['site.json', 'cleanblogarticleindex.json', 'cleanblogarticle.json']

    def test_article_index_articles_property_returns_num_child_page(self):
        num_child_pages = CleanBlogArticlePage.objects.live().descendant_of(self.article_index_page).count()
        self.assertEqual(num_child_pages, 2)
        self.assertEqual(num_child_pages, len(self.article_index_page.articles))

    def test_article_knows_next_sibling(self):
        self.assertEqual(self.article_page.next_sibling.specific, self.article_page_two)

    def test_article_knows_previous_sibling(self):
        self.assertEqual(self.article_page_two.previous_sibling.specific, self.article_page)
