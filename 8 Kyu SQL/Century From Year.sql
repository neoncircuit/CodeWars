--your statment goes here--
select y.*,
      ceil(y.yr/100.0) as century
from years as y