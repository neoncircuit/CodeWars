select 
  g.name,
  g.greeting,
  substring(greeting from '#(\d+)') as user_id
from 
  greetings as g