declare @id int 
select @id = 1
while @id >=1 and @id <= 100
begin
    insert into studapp_student values(@id, 'jill' + convert(varchar(5), @id), 'jack' + convert(varchar(5), @id),1995-01-08, 'jill' + convert(varchar(5), @id) + 'gmail.com','jon' + convert(varchar(5), @id), rand(1111111111,9999999999), 2021-01-17, 2021-01-25, 2004, 4)
    select @id = @id + 1
end
