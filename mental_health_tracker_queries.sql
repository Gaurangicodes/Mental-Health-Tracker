CREATE DATABASE mental_health_tracker; 
USE mental_health_tracker; 
CREATE TABLE users ( 
user_id INT AUTO_INCREMENT PRIMARY KEY, 
name VARCHAR(100) NOT NULL, 
email VARCHAR(100) NOT NULL UNIQUE 
); 
CREATE TABLE letters ( 
letter_id INT AUTO_INCREMENT PRIMARY KEY, 
user_id INT, 
letter_text TEXT, 
to_self ENUM('Past', 'Present', 'Future') NOT NULL, 
date_written TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
FOREIGN KEY (user_id) REFERENCES users(user_id) 
); 
CREATE TABLE mood_tracker ( 
mood_id INT AUTO_INCREMENT PRIMARY KEY, 
    user_id INT, 
    mood VARCHAR(50), 
    date_recorded TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    FOREIGN KEY (user_id) REFERENCES users(user_id) 
); 
CREATE TABLE worry_box ( 
    worry_id INT AUTO_INCREMENT PRIMARY KEY, 
    user_id INT, 
    worry_text TEXT, 
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    FOREIGN KEY (user_id) REFERENCES users(user_id) 
); 
CREATE TABLE gratitude_journal ( 
    journal_id INT AUTO_INCREMENT PRIMARY KEY, 
    user_id INT, 
    gratitude_entry TEXT, 
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    FOREIGN KEY (user_id) REFERENCES users(user_id) 
); 
CREATE TABLE affirmations ( 
    affirmation_id INT AUTO_INCREMENT PRIMARY KEY, 
    quote TEXT 
); 
CREATE TABLE bucket_list ( 
bucket_id INT AUTO_INCREMENT PRIMARY KEY, 
user_id INT, 
item TEXT, 
date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
FOREIGN KEY (user_id) REFERENCES users(user_id) 
); 
INSERT INTO affirmations (quote) VALUES 
('To be beautiful means to be yourself.'), 
('This too shall pass.'), 
('Enjoy the litte things!'), 
('Making mistakes is bigger than faking perfections.'), 
('It is okay to say no to unnecessary crazy.'), 
('Que sera sera. Whatever will be, will be.'), 
('Smile more, Worry less.'), 
('Life is a journey, not a race.'), 
('You are worthy of the time it takes to do things that heal your heart.'), 
('In a world where you can be anything, Be kind.'), 
('Be a fountain, not a drain.'), 
('Descisions determine destiny.'), 
('You were not born to just pay bills and die.'), 
('Focus on the step in front of you, not the whole staircase.'), 
('Pursue wholeness instead of perfection. You will find it very liberating.'), 
('I know you are scared, but you can handle this.'), 
('Do not let the seeds stop you from enjoying the watermelon.'), 
('You are more than what people see.'), 
('You can always choose to be happy.'), 
('Life is way better when you are laughing.');
