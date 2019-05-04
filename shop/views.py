from django.views.generic import TemplateView
from shop import models


class PublicationsListView(TemplateView):
    template_name = 'shop/publications.tpl'
    model = None
    parent = None

    def get_by_id(self, publication_id):
        return self.model.objects.filter(
            **{f'{self.parent}_id': publication_id}
        ).all()

    def get_all(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publication_id = kwargs.get('publication_id')

        updates = {'title': self.model.__name__.lower()}
        if publication_id:
            updates['publications'] = self.get_by_id(publication_id)
        else:
            updates['publications'] = self.get_all()

        context.update(updates)

        return context


class IndexView(PublicationsListView):
    model = models.Category


class CategoryView(PublicationsListView):
    model = models.Item
    parent = 'category'


class ItemView(TemplateView):
    template_name = 'shop/item.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_id = kwargs.get('item_id')
        item = models.Item.objects.get(id=item_id)
        context.update({'item': item})
        return context