**teachers_to_main的主要功能**

> 1. 作为所有函数的入口
>
> 2. 从现代邮政学院的导师主页获取所有老师的网页链接，并将网页信息都保存在teachers_page.txt里面
>
> 3. 再从网页信息中获得老师的个人简介以及姓名（利用正则表达式从个人简介里面获取），并将姓名放在teachers_name.xlsx里面
>
> 4. 调用extraction_utils以及extract_version_1

**extraction_utils的主要功能**

> 1. 从teachers_page.txt中读取老师姓名，将中文转换为英文（可以说是拼音）
>
> 2. 将老师的英文名字写进teacher.txt里面

**extract_version_1的主要功能**

> 1. 根据teacher.txt里面的信息在dblp对老师检索，进入老师的dblp论文界面
>
> 2. 获取老师的论文信息
>
> 3. 对论文信息进行分别处理，获取论文的具体情况，一作、二作、论文名字、期刊名字、页码等
>
> 4. 将信息写进teacher_information_other_test.json文件中

**add文件夹**

这个模块暂时没有加入到整个工程中，只是进行了测试，测试可以通过

> 主要是实现精确查找，避免重名对结果的影响
