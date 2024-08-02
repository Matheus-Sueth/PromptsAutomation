import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk as ttk
from dataclasses import dataclass
import os
from genesys.api import Genesys
from src.functions import upload_user_prompts


def tamanho_janela(menu: tkinter.Tk, win_width: int, win_height: int, color_background: str, icon_path: str = '') -> None:
    screen_width = menu.winfo_screenwidth()
    screen_height = menu.winfo_screenheight()
    start_x = int((screen_width / 2) - (win_width / 2))
    start_y = int((screen_height / 2) - (win_height / 2))
    #menu.iconbitmap(icon_path)
    menu['bg'] = color_background
    menu.geometry(f"{win_width}x{win_height}+{start_x}+{start_y}")
    menu.resizable(False, False)
    menu.update()


@dataclass
class Cor:
    ROSA_ESCURO: str = '#910142'
    ROSA_MAGENTA: str = '#6c043c'
    MAGENTA_ESCURO: str = '#210123'
    AMARELO_CLARO: str = '#fef7d5'
    CIANO: str = '#0ec0c1'


@dataclass
class Fonte:
    LABEL: tuple = ('Arial Black', 24)
    BUTTON: tuple = ('Arial', 18)


@dataclass
class Estilo:
    COR = Cor()
    FONTE = Fonte()


class Tela:
    def __init__(self) -> None:
        pass


class PA(Tela):
    def __init__(self, root: tkinter.Tk):
        self.root = root
        self.root.title('Prompts Automation')
        tamanho_janela(self.root, 600, 400, Estilo.COR.MAGENTA_ESCURO)
        self.frame_principal = tkinter.Frame(self.root, bg=Estilo.COR.MAGENTA_ESCURO)
        self.frame_principal.pack()

        self.label_aplicativo = tkinter.Label(
            self.frame_principal,
            text='Automatização dos prompts',
            background=Estilo.COR.MAGENTA_ESCURO,
            fg=Estilo.COR.AMARELO_CLARO,
            width=30,
            font=Estilo.FONTE.LABEL
        ).pack(pady=70)

        self.lista = ttk.Combobox(
            self.frame_principal,
            values=list(Genesys.DADOS.keys()),
            foreground=Cor.MAGENTA_ESCURO,
            width=30,
            font=('Arial Black', 12)
        )
        self.lista.pack()

        self.frame_botoes = tkinter.Frame(self.frame_principal, bg=Cor.MAGENTA_ESCURO)
        self.frame_botoes.pack()

        self.botao_ajuda = tkinter.Button(
            self.frame_botoes,
            text='AJUDA',
            bg=Cor.CIANO,
            fg=Cor.AMARELO_CLARO,
            height=2,
            width=15,
            font=('Arial', 18),
            border=15,
            command=self.escolher_org
        )
        self.botao_ajuda.pack(pady=10)

    def escolher_org(self):
        self.org = self.lista.get()
        self.ir_tela_EscolheFuncao()

    def ir_tela_EscolheFuncao(self):
        self.frame_principal.pack_forget()
        tela = EscolheFuncao(self.root, self, Genesys(self.org))
        tela.tela_EscolheFuncao()

    def tela_SM(self):
        self.frame_principal.pack()


class EscolheFuncao(Tela):
    def __init__(self, master: tkinter.Tk, tela_anterior: PA, api: Genesys):
        self.master = master
        self.tela_anterior = tela_anterior
        self.api_genesys = api
        self.master.title('Prompts Automation')
        tamanho_janela(self.master, 600, 400, Estilo.COR.MAGENTA_ESCURO)
        self.frame_principal = tkinter.Frame(self.master, bg=Estilo.COR.MAGENTA_ESCURO)
        self.frame_principal.pack()

        self.label_aplicativo = tkinter.Label(
            self.frame_principal,
            text='Escolha sua função',
            background=Estilo.COR.MAGENTA_ESCURO,
            fg=Estilo.COR.AMARELO_CLARO,
            width=30,
            font=Estilo.FONTE.LABEL
        ).pack(pady=70)

        opcoes = ['upload_user_prompts_for_ura','upload_user_prompts_for_ura2','upload_user_prompts_for_ura3','upload_user_prompts','upload_user_prompts_for_bot']

        self.lista = ttk.Combobox(
            self.frame_principal,
            values=opcoes,
            foreground=Cor.MAGENTA_ESCURO,
            width=30,
            font=('Arial Black', 12)
        )
        self.lista.pack()

        self.frame_botoes = tkinter.Frame(self.frame_principal, bg=Cor.MAGENTA_ESCURO)
        self.frame_botoes.pack()

        self.botao_ajuda = tkinter.Button(
            self.frame_botoes,
            text='ESCOLHER',
            bg=Cor.CIANO,
            fg=Cor.AMARELO_CLARO,
            height=2,
            width=15,
            font=('Arial', 18),
            border=15,
            command=self.funcao_escolhida
        )
        self.botao_ajuda.pack(pady=10)

    def funcao_escolhida(self):
        self.ir_tela_UploadUserPrompts()

    def ir_tela_UploadUserPrompts(self):
        self.frame_principal.pack_forget()
        tela = UploadUserPrompts(self.master, self, self.api_genesys)
        tela.tela_UploadUserPrompts()

    def tela_EscolheFuncao(self):
        self.frame_principal.pack()


class UploadUserPrompts(Tela):
    def __init__(self, master: tkinter.Tk, tela_anterior: EscolheFuncao, api: Genesys):
        self.master = master
        self.tela_anterior = tela_anterior
        self.api_genesys = api
        self.master.title('Upload User Prompts')
        tamanho_janela(self.master, 600, 400, Estilo.COR.MAGENTA_ESCURO)
        self.diretorio = ''
        self.frame_principal = tkinter.Frame(self.master, bg=Estilo.COR.MAGENTA_ESCURO)
        self.frame_principal.pack()

        self.botao_ajuda = tkinter.Button(
            self.frame_principal,
            text='DIRETORIO',
            bg=Cor.CIANO,
            fg=Cor.AMARELO_CLARO,
            height=2,
            width=15,
            font=('Arial', 18),
            border=15,
            command=self.escolher_diretorio
        )
        self.botao_ajuda.pack(pady=10)

        self.frame_segundario = tkinter.Frame(self.frame_principal, bg=Estilo.COR.MAGENTA_ESCURO)
        self.frame_segundario.pack()

        self.label = ttk.Label(
            self.frame_segundario,
            text='IVR',
            background=Cor.CIANO,
            foreground=Cor.AMARELO_CLARO,
            width=15,
            font=('Arial', 18),
            border=15,
        )
        self.label.pack(pady=10)

        self.entrada = ttk.Entry(
            self.frame_segundario,
            foreground=Cor.CIANO,
            width=15,
            font=('Arial', 18)
        )
        self.entrada.pack(pady=10)

        self.botao_ajuda = tkinter.Button(
            self.frame_principal,
            text='AJUDA',
            bg=Cor.CIANO,
            fg=Cor.AMARELO_CLARO,
            height=2,
            width=15,
            font=('Arial', 18),
            border=15,
            command=self.upload
        )
        self.botao_ajuda.pack(pady=10)

    def escolher_diretorio(self) -> None:
        path = tkinter.filedialog.askdirectory(title='Selecione o diretório com os prompts', initialdir='/')
        if path:
            tkinter.messagebox.showinfo(title='INFORMAÇÃO', message='Diretório escolhido com sucesso')
            self.diretorio = path
        else:
            tkinter.messagebox.showerror(title='ERRO', message='Falha na escolha do diretório')
            self.diretorio = ''

    def upload(self):
        if os.path.exists(self.diretorio):
            tkinter.messagebox.showwarning(title='ALERTA', message='Diretório não foi selecionado ou é inválido')
            return None
        
        ivr = self.entrada.get()

        if len(ivr) != 6 or not ivr.isnumeric():
            tkinter.messagebox.showwarning(title='ALERTA', message='Campo IVR deve ter 6 caracteres exatos e deve ser preenchido apenas de números')
            return None
        
        upload_user_prompts(self.api_genesys, self.diretorio, f'IVR-{ivr}')
        

    def tela_UploadUserPrompts(self):
        self.frame_principal.pack()



#upload_user_prompts
root = tkinter.Tk()
app = PA(root)
app.root.mainloop()