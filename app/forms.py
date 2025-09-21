from django import forms
from .models import Raffle

class RaffleForm(forms.ModelForm):
    class Meta:
        model = Raffle
        fields = ['title', 'description', 'image', 'price', 'total_tickets', 'status', 'draw_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-[#f7f7f7] text-xs focus:ring-blue-500 focus:border-blue-500'}),
            'description': forms.Textarea(attrs={'class': 'block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-[#f7f7f7] text-xs focus:ring-blue-500 focus:border-blue-500', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 p-2'}),
            'price': forms.NumberInput(attrs={'class': 'block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-[#f7f7f7] text-xs focus:ring-blue-500 focus:border-blue-500'}),
            'total_tickets': forms.NumberInput(attrs={'class': 'block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-[#f7f7f7] text-xs focus:ring-blue-500 focus:border-blue-500'}),
            'status': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}),
            'draw_date': forms.DateTimeInput(
                attrs={
                    'class': 'block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-[#f7f7f7] text-xs focus:ring-blue-500 focus:border-blue-500',
                    'type': 'datetime-local',
                },
                format='%Y-%m-%dT%H:%M'
            ),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.draw_date:
            self.initial['draw_date'] = self.instance.draw_date.strftime('%Y-%m-%dT%H:%M')
