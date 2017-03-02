# book_store
use python3, Tkinter and sqlite to create a book store desktop application

![alt text](https://github.com/smalltide/book_store/blob/master/screenshot.gif "book_store")

1. python3
2. Tkinter
3. sqlite3

```
  > git@github.com:smalltide/book_store.git
  > cd book_store
  > python3 app.py
```

Wrap python script to executable application
```
  > pip3 install pyinstaller (for windows .exe)
  > pyinstaller --onefile --windowed app.py
  >
  >
  > pip3 install py2app
  > py2applet --make-setup app.py
  > python3 setup.py py2app
```

A program that stores this book information:
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add Entry
Update
Delete
Close
