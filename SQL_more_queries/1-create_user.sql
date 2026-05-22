-- Create user user_0d_1 with all priviliges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
INDENTIFIED BY 'user_0d_1_pwd';

GRANT ON PRIVILIGES ON *.* TO USER 'user_0d_1'@localhost
FLUSH PRIVILIGES;
