# GUI Application automation and testing library
# Copyright (C) 2006-2018 Mark Mc Mahon and Contributors
# https://github.com/pywinauto/pywinauto/graphs/contributors
# http://pywinauto.readthedocs.io/en/latest/credits.html
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of pywinauto nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Run some automations to test things"""
from __future__ import unicode_literals
from __future__ import print_function

import os.path
import sys

try:
    from pywinauto import application
except ImportError:
    pywinauto_path = os.path.abspath(__file__)
    pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
    sys.path.append(pywinauto_path)
    from pywinauto import application

def run_notepad():
    """Run notepad and do some small stuff with it"""
    app = application.Application()

    ## for distribution we don't want to connect to anybodies application
    ## because we may mess up something they are working on!
    #try:
    #    app.connect_(path = r"c:\windows\system32\notepad.exe")
    #except application.ProcessNotFoundError:
    #    app.start_(r"c:\windows\system32\notepad.exe")
    app.start(r"notepad.exe")

    app.Notepad.menu_select("Arquivo->Configurar Página")

    # ----- Page Setup Dialog ----
    # Select the 4th combobox item
    app['Configurar Página'].SizeComboBox.select(4)

    # Select the 'Letter' combobox item or the Letter
    try:
        app['Configurar Página'].SizeComboBox.select("Carta")
    except ValueError:
        app['Configurar Página'].SizeComboBox.select('Carta (8.5" x 11")')

    app['Configurar Página'].SizeComboBox.select(2)

    app['Configurar Página'].OK.click()

    # type some text - note that extended characters ARE allowed
    app.Notepad.Edit.set_edit_text("I am typing s\xe4me text to Notepad\r\n\r\n"
        "And then I am going to quit")

    app.Notepad.Edit.right_click()
    # app.PopupMenu.menu_item("Sentid&o de leitura da direita para a esquerda").click()
    app.PopupMenu.menu_item("Sentid&o de leitura da direita para a esquerda").click_input()

    # Try and save
    app.Notepad.menu_select("Arquivo->Salvar Como")
    app["Salvar como"].ComboBox3.select("UTF-8")
    app["Salvar como"].Edit.set_edit_text(rf"{os.getcwd()}\Example-utf8.txt")
    app["Salvar como"].Salvar.close_click()
    app.Notepad.menu_select("Arquivo->Sair")

if __name__ == "__main__":
    run_notepad()
