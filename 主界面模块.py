import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView


class FileTransferApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.status_label = Label(text="选择传输方式")

        self.face_to_face_button = Button(text="面对面无线传送")
        self.remote_button = Button(text="远程无线传送")
        self.exit_button = Button(text="退出", size_hint_y=None, height=50)

        self.face_to_face_button.bind(on_press=self.face_to_face_transfer)
        self.remote_button.bind(on_press=self.remote_transfer)
        self.exit_button.bind(on_press=self.stop)

        self.layout.add_widget(self.status_label)
        self.layout.add_widget(self.face_to_face_button)
        self.layout.add_widget(self.remote_button)
        self.layout.add_widget(self.exit_button)

        return self.layout

    def face_to_face_transfer(self, instance):
        self.status_label.text = "PC端热点开启中..."
        # 添加热点创建和连接代码
        self.search_and_connect_pc_hotspot()

    def remote_transfer(self, instance):
        self.status_label.text = "请输入远程服务器信息"
        # 添加远程服务器连接代码
        self.connect_to_remote_server()

    def search_and_connect_pc_hotspot(self):
        # 模拟热点搜索和连接
        self.status_label.text = "搜索并连接到PC端热点..."
        # 假设成功连接
        self.status_label.text = "已连接到PC端热点"
        self.choose_file_to_send()

    def connect_to_remote_server(self):
        # 模拟远程服务器连接
        self.status_label.text = "连接到远程服务器..."
        # 假设成功连接
        self.status_label.text = "已连接到远程服务器"
        self.verify_identity()

    def verify_identity(self):
        # 模拟身份验证
        self.status_label.text = "验证身份信息..."
        # 假设验证成功
        self.status_label.text = "身份验证成功"
        self.choose_file_to_send()

    def choose_file_to_send(self):
        self.filechooser = FileChooserListView(filters=['*.*'])
        self.layout.clear_widgets()
        self.layout.add_widget(self.filechooser)

        send_button = Button(text="发送文件", size_hint_y=None, height=50)
        back_button = Button(text="返回", size_hint_y=None, height=50)
        exit_button = Button(text="退出", size_hint_y=None, height=50)

        send_button.bind(on_press=self.send_file)
        back_button.bind(on_press=self.return_to_main)
        exit_button.bind(on_press=self.stop)

        self.layout.add_widget(send_button)
        self.layout.add_widget(back_button)
        self.layout.add_widget(exit_button)
        self.layout.add_widget(self.status_label)

    def send_file(self, instance):
        selected_file = self.filechooser.selection
        if selected_file:
            file_path = selected_file[0]
            self.status_label.text = f"选择的文件: {file_path}"
            # 添加文件传输代码
            self.transfer_file(file_path)

    def transfer_file(self, file_path):
        # 模拟文件传输过程
        self.status_label.text = "文件传输中..."
        # 假设传输成功
        self.status_label.text = "文件传输成功"

    def return_to_main(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(self.status_label)
        self.layout.add_widget(self.face_to_face_button)
        self.layout.add_widget(self.remote_button)
        self.layout.add_widget(self.exit_button)


if __name__ == '__main__':
    FileTransferApp().run()
