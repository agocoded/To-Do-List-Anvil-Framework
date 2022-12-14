from ._anvil_designer import AllCompletedTaskTemplateTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AllCompletedTaskTemplate(AllCompletedTaskTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    description = str(self.item['description'])
    
    if self.item['completed on']:
      current_time = self.item['completed on'].strftime('%d %b %Y %I:%M%p')
      alert(description + '\n'+ 'Task Completed on: ' + current_time)
    else:
      alert(description)

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
   


