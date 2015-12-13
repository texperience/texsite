# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.blocks import RichTextBlock

from texsite.core.models import BasePage
from texsite.core.blocks import HeadingBlock, ImageBlock, IntroBlock, QuoteBlock


class CleanBlogArticlePage(BasePage):
    """Clean blog article page"""
    # Page model fields
    body = StreamField([
        ('intro', IntroBlock()),
        ('heading', HeadingBlock(template="texsitecleanblog/blocks/heading.html")),
        ('paragraph', RichTextBlock()),
        ('image', ImageBlock(template="texsitecleanblog/blocks/image.html")),
        ('quote', QuoteBlock(template="texsitecleanblog/blocks/quote.html")),
    ])

    # Editor interface configuration
    content_panels = BasePage.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = _('Clean Blog Article Page') + ' (' + __package__ + ')'


class CleanBlogArticleIndexPage(BasePage):
    """Clean blog article index page"""
    # Page model fields
    body = StreamField([
        ('intro', IntroBlock()),
    ])

    @property
    def articles(self):
        # Get list of live article pages that are descendants of this page by sort order
        return CleanBlogArticlePage.objects.live().descendant_of(self).order_by("path")

    def get_context(self, request):
        # Get articles
        articles = self.articles

        # Pagination
        page = request.GET.get("page")
        paginator = Paginator(articles, 4)

        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        # Update template context
        context = super(CleanBlogArticleIndexPage, self).get_context(request)
        context["articles"] = articles

        return context

    # Editor interface configuration
    content_panels = BasePage.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = _('Clean Blog Article Index Page') + ' (' + __package__ + ')'
