from ._anvil_designer import AllTasksTemplateTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...TaskEdit import TaskEdit
from datetime import datetime

class AllTasksTemplate(AllTasksTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_edit_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert(TaskEdit(item = self.item), title="Edit Your Task Details", large=True)
    self.refresh_data_bindings()   

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if (self.item['done']) == True:
      self.item['completed on'] = datetime.now()


  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    description = str(self.item['description'])
    
    if self.item['completed on']:
      current_time = self.item['completed on'].strftime('%d %b %Y %I:%M%p')
      alert(description + '\n'+ 'Task Completed on: ' + current_time)
    else:
      alert(description)

  def delete_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.item.delete()
    self.remove_from_parent()
    #self.refresh_data_bindings()




