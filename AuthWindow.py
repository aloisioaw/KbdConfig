from Tkinter import *

class popupWindow(object):

	def __init__(self,master):
		self.master = master
		self.master.resizable(width=FALSE, height=FALSE)
		self.master.minsize(width=160, height=80)
		self.master.title("Senha de Root")
		self.lblSenha = Label(master,text = "Senha:")
		self.lblSenha.grid(row = 0, column = 0, columnspan=2)
		self.txtSenha = Entry(master, width=25, show="*")
		self.txtSenha.bind("<Return>", self.pressionou_enter)
		self.txtSenha.bind("<Escape>", self.pressionou_esc)
		self.txtSenha.grid(row = 1, column = 0, columnspan=2, padx=5, pady=10)
		self.txtSenha.focus()
		self.btnOk = Button(master,text = 'Ok', width=8, command = self.cleanup).grid(row = 2, column = 0, padx=5, pady=5)
		self.btnCancelar = Button(master,text = 'Cancelar', width=8, command = self.cancelar).grid(row = 2, column = 1, padx=5, pady=5)

	def cleanup(self):
		self.senha = self.txtSenha.get()
		self.master.destroy()

	def cancelar(self):
		self.master.destroy()

	def pressionou_esc(self, event):
		self.master.destroy()

	def pressionou_enter(self, event):
		self.senha = self.txtSenha.get()
		self.master.destroy()


if __name__ == "__main__":
	root = Tk()
	m = popupWindow(root)
	root.mainloop()