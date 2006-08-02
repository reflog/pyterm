# GTK/Gnome imports
import pygtk
pygtk.require('2.0')
import gtk,pango,vte,gconf


import settings as conf    

def tab_move_left(main, sender, event):
    pn = main.nb.get_current_page()
    main.nb.reorder_child(main.nb.get_nth_page(pn),pn-1)

def tab_move_right(main, sender, event):
    pn = main.nb.get_current_page()
    if pn+1 == main.nb.get_n_pages():
        main.nb.reorder_child(main.nb.get_nth_page(pn),0)
    else:
        main.nb.reorder_child(main.nb.get_nth_page(pn),pn+1)

def tab_shift_left(main, sender, event):
    pn = main.nb.get_current_page() - 1
    main.nb.set_current_page(pn)

def tab_shift_right(main, sender, event):
    pn = main.nb.get_current_page() + 1
    if pn == main.nb.get_n_pages():
        pn = 0
    main.nb.set_current_page(pn)

def tab_select(n, main, sender, event):
    main.nb.set_current_page(n-1)

def show_settings(main, sender, event):
    print 'hey hey'

we_are_fs = False

def fullscreen(main, sender, event):
    global we_are_fs
    we_are_fs = not we_are_fs
    if we_are_fs:
        main.window.fullscreen()
    else:
        main.window.unfullscreen()

def tab_new(main, sender, event):
    w = main.new_tab()
    pn = main.nb.page_num(w)
    main.nb.set_current_page(pn)
    main.window.set_focus(w)

def tab_close(main, sender, event):
    main.remove_book_by_n( main.nb.get_current_page() )

def command_by_key(b, key, state):
    for v in b.values():
        (k,s) = gtk.accelerator_parse(v['key'])
        if k == key and s == state:
            return v['command']
    

def handle_key_press(main, sender, event):
    cmd = command_by_key(conf.read_bindings(), event.keyval, event.state)
    if cmd:
        cmd(main, sender,event)
        return True
    return False