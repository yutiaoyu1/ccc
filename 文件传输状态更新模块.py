from kivy.uix.label import Label

class FileSelectorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.filechooser = FileChooserListView()
        select_button = Button(text="Select File", size_hint_y=None, height=50)
        select_button.bind(on_press=self.select_file)
        self.status_label = Label(text="Status: Waiting for file selection")
        self.layout.add_widget(self.filechooser)
        self.layout.add_widget(select_button)
        self.layout.add_widget(self.status_label)
        return self.layout

    def select_file(self, instance):
        selected_file = self.filechooser.selection
        if selected_file:
            self.status_label.text = f"Selected file: {selected_file[0]}"
            # 这里可以添加文件处理代码，例如读取或打包文件

if __name__ == '__main__':
    FileSelectorApp().run()
