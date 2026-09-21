<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# venv 手把手实训：同一份应用，为什么换环境就出错

你有一份主机辅助程序，旧项目要求它输出第一版协议，新项目已换成第二版。源码相同，运行结果却随电脑变化。本实训让你亲手制造问题，再用环境隔离、应用测试和依赖重建定位原因。无需开发板、SDK 或 Python 语法课程；需要 Windows Python 3.12 和 UCRT64 Bash，检查方法见[实验准备](../../../P00_实验准备.md)。

**venv** 是 Python 自带的虚拟环境创建模块；虚拟环境保存独立安装的第三方包。**pip** 是包安装工具；**解释器** 是执行 Python 的程序。项目目录分开不会自动隔离包，安装和运行必须使用对应环境的解释器。

本页可独立执行，不要求先做 P01～P04，也不复用它们的 A/B。预计 45～75 分钟。每步先预测，再执行并对照结果；普通命令失败就停下处理，只有标为“故意失败”的步骤允许非零退出。首次准备工具需要网络，本地包准备好后可以断网。

## 1. 复制一份应用与测试模板

当前位置：本仓库根目录，新开 UCRT64 Bash。先检查教材存在，再复制练习副本：

```bash
test -f learning/python/venv/labs/application/main.py
echo $?
py -3.12 --version
mkdir -p build/learning-tools
mkdir build/learning-tools/venv-practice
cp -R learning/python/venv/labs/application build/learning-tools/venv-practice/app
cp -R learning/python/venv/labs/package_v1 build/learning-tools/venv-practice/package_v1
cp -R learning/python/venv/labs/package_v2 build/learning-tools/venv-practice/package_v2
cd build/learning-tools/venv-practice
pwd
```

`test -f` 检查文件存在，成功无输出；`echo $?` 查看上一条命令的退出码，0 为成功。`py -3.12` 用 Windows 启动器明确选择解释器。`mkdir -p` 准备父目录；第二个 mkdir 故意不加 `-p`，已有练习时会报 File exists。此时停止，保留原目录并换新名字，不继续复制。`cp -R` 复制目录树，后续只改副本；`cd` 改变相对路径的起点，`pwd` 应以 venv-practice 结尾。

打开下列副本，先认清源码、安装要求和测试各自的责任：

| 副本位置 | 做什么 | 教材原件 |
| --- | --- | --- |
| `app/main.py` | 调用 `greet("board")`，打印问候语 | [应用](application/main.py) |
| `app/tests/test_greeting.py` | 两条断言要求默认名与 board 名都返回 v1 协议 | [测试模板](application/tests/test_greeting.py) |
| `app/requirements.txt` | 要求安装 `lab-greeting==1.0.0` | [依赖模板](application/requirements.txt) |
| `package_v1/pyproject.toml` | 声明包名、版本及打包工具 | [包配置](package_v1/pyproject.toml) |
| `package_v1/src/lab_greeting/__init__.py` | 实现第一版 greet 函数 | [函数](package_v1/src/lab_greeting/__init__.py) |

分发包名 lab-greeting 用于安装；导入名 lab_greeting 用于代码，不能把连字符直接写进导入语句。可复用模板是“应用、requirements、tests”三部分，环境和安装产物随后生成，不与源码混放。

## 2. 创建环境，证明真正运行的是谁

当前位置：`build/learning-tools/venv-practice`，此后一直留在这里。

```bash
py -3.12 -m venv a b builder
a/Scripts/python.exe -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
a/Scripts/python.exe -m pip --version
cat a/pyvenv.cfg
```

`-m venv` 让选定 Python 运行标准库模块，a、b、builder 是三个独立目录；成功通常无输出。Windows Python 的环境程序在 Scripts 中，使用 Bash 不会把它变成 Linux 的 bin 布局。builder 稍后负责打包，A/B 只装应用依赖。

`-c` 执行短代码；`sys.executable` 显示实际解释器，`sys.prefix` 是环境目录，`sys.base_prefix` 是基础 Python 目录。预期解释器属于 a，比较结果为 True。`-m pip` 将安装器绑定到 A，输出路径也应属于 a；单独输入 pip 可能选中另一份程序。`cat` 读取环境配置，关注 `include-system-site-packages = false`：默认不开放基础 Python 的第三方包目录。

对照 [Python 的 How venvs work](https://docs.python.org/3.12/library/venv.html#how-venvs-work)，重点核对“运行时前缀”和“激活修改 PATH”分别回答什么问题。

先预测：没有激活 A，为什么已经可以用 A？因为路径明确指定了执行程序。再观察激活：

```bash
source a/Scripts/activate
python -c "import sys; print(sys.executable)"
b/Scripts/python.exe -c "import sys; print(sys.executable)"
deactivate
```

`source` 在当前 Bash 执行激活文件，将 A 的程序目录放到命令搜索路径 PATH 前面；短命令 python 选 A，明确的 B 路径仍选 B。`deactivate` 恢复终端设置，不卸载包、不删除环境。后面继续使用明确路径。

新环境若缺 pip，使用 `a/Scripts/python.exe -m ensurepip --upgrade`；ensurepip 是 Python 随附的 pip 引导模块。不要用系统 pip 代替它给 A 安装。

## 3. 先让测试失败：环境为空时缺少什么

源码存在，A 却还没安装它需要的包。下面两次运行**故意失败**：

```bash
a/Scripts/python.exe app/main.py
echo $?
a/Scripts/python.exe -m unittest discover -s app/tests -v
echo $?
```

预期退出码非零，错误含 `ModuleNotFoundError: No module named 'lab_greeting'`。这说明 A 找不到依赖，不是解释器本身坏了。

**unittest** 是标准库测试框架，无须安装。`discover` 查找测试文件，`-s app/tests` 指定起始目录，`-v` 逐项显示名称；`assertEqual` 比较实际值和期望值。此时连测试模块都不能导入，报告 ERROR；后面会看到“能导入但行为不符”的 FAIL。这两种结果对应不同排查层次。

不修改测试来掩盖错误，也不安装到全局 Python；下一步生成安装包并装到 A。

## 4. 将源码变成两份本地安装包

**wheel** 是 Python 可安装归档格式，后缀为 .whl；**setuptools** 是本例的打包工具。pyproject.toml 中 build-system 分区选择构建后端，project 分区声明包名、版本等信息。Python 3.12 新环境不自带 setuptools，因此显式准备：

```bash
builder/Scripts/python.exe -m pip download --only-binary=:all: --no-deps --dest bootstrap setuptools==80.9.0
builder/Scripts/python.exe -m pip install --no-index --find-links bootstrap setuptools==80.9.0
builder/Scripts/python.exe -m pip wheel --no-index --no-deps --no-build-isolation --wheel-dir wheelhouse ./package_v1
builder/Scripts/python.exe -m pip wheel --no-index --no-deps --no-build-isolation --wheel-dir wheelhouse ./package_v2
ls wheelhouse
```

第一条是本路线唯一必需的联网下载；若已从可信来源取得同版本 wheel，放入 bootstrap 后从第二条继续。下载失败先修复来源或网络，不执行依赖步骤。

| 动作或参数 | 为什么使用 | 修改了什么 |
| --- | --- | --- |
| `download --dest bootstrap` | 保存构建工具安装包，供离线复用 | 新增文件，尚未安装 |
| `--only-binary=:all:` | 要求现成 wheel，避免构建工具本身 | 找不到 wheel 时失败 |
| `install --no-index --find-links bootstrap` | 禁止查询在线索引，只搜索本地目录 | builder 安装 setuptools |
| `wheel --wheel-dir wheelhouse` | 从源码产生安装文件 | 新增教学包 v1/v2 wheel |
| `--no-build-isolation` | 使用 builder 已有后端 | 不另建临时构建环境，缺后端就失败 |
| `--no-deps` | 本例没有运行依赖，不继续处理依赖包 | 有传递依赖的实际工程不能盲目照搬 |

预期出现 `lab_greeting-1.0.0-py3-none-any.whl` 与 `lab_greeting-2.0.0-py3-none-any.whl`。py3-none-any 是本例纯 Python 包的兼容标记，不代表所有二进制扩展也能跨平台。打包在复制品里产生的 build、egg-info 元数据不会污染教材原件。

## 5. 同一个应用，在 A 通过，在 B 失败

```bash
a/Scripts/python.exe -m pip install --no-index --find-links wheelhouse -r app/requirements.txt
b/Scripts/python.exe -m pip install --no-index --find-links wheelhouse lab-greeting==2.0.0
a/Scripts/python.exe app/main.py
b/Scripts/python.exe app/main.py
a/Scripts/python.exe -m unittest discover -s app/tests -v
```

`-r` 读取安装要求文件，`==` 固定准确版本。A 接受应用声明的 v1，B 故意安装 v2。应用依次输出 `hello board from v1`、`hello board from v2`。A 测试应显示 `Ran 2 tests` 和 `OK`；OK 是 unittest 表示全部测试成功的输出标识符。

B 能运行，是否就代表旧应用可以接受它？

```bash
b/Scripts/python.exe -m pip check
b/Scripts/python.exe -m unittest discover -s app/tests -v
echo $?
```

pip check 应输出 `No broken requirements found.`，它只检查已安装包声明的依赖关系，不拿 app/requirements.txt 校验应用契约，也不执行测试。随后 unittest **故意失败**，预期 `FAILED (failures=2)`，差异显示 v2 与 v1 不同。可安装、可导入、业务兼容是三个判断。

按应用声明恢复 B，再跑同一套测试：

```bash
b/Scripts/python.exe -m pip install --no-index --find-links wheelhouse -r app/requirements.txt
b/Scripts/python.exe -m unittest discover -s app/tests -v
```

预期 B 降到 1.0.0 并通过。固定版本安装既能升级也能降级；真实升级应审查业务变化，更新依赖声明与测试，不能仅凭 pip 成功就接受新版。

## 6. 查证安装位置，卸载后再恢复

```bash
a/Scripts/python.exe -m pip list
a/Scripts/python.exe -m pip show lab-greeting
a/Scripts/python.exe -c "import lab_greeting; print(lab_greeting.__file__)"
b/Scripts/python.exe -m pip uninstall -y lab-greeting
b/Scripts/python.exe app/main.py
echo $?
a/Scripts/python.exe -m unittest discover -s app/tests -v
b/Scripts/python.exe -m pip install --no-index --find-links wheelhouse -r app/requirements.txt
b/Scripts/python.exe app/main.py
```

list 查版本，show 查分发包安装位置，模块属性 __file__ 指向**本次实际导入**的文件；A 的后两项应落在 a 的 site-packages 中。当前目录里的同名文件可能抢先被导入，所以只有 show 不足以证明运行来源。

`uninstall -y` 在明确指定的 B 中免交互确认卸载；接着 B 的运行故意报缺包，A 的测试仍通过。最后重装 B 并运行，恢复为 v1。它证明卸载只影响一个环境，不删除源码。

如果安装成功仍导入失败，先核对安装和运行是否使用同一解释器，再查 show 与 __file__，不要反复盲装。同名遮蔽的进一步实验见[P04](../P04_排错与工程使用习惯.md)。

## 7. 用记录重建环境，再制造版本冲突

```bash
a/Scripts/python.exe -m pip freeze > requirements-snapshot.txt
cat requirements-snapshot.txt
py -3.12 -m venv rebuilt
rebuilt/Scripts/python.exe -m pip install --no-index --find-links wheelhouse -r requirements-snapshot.txt
rebuilt/Scripts/python.exe -m unittest discover -s app/tests -v
```

freeze 报告当前安装状态；Bash 的 `>` 保存输出，会覆盖同名旧文件。A 没装构建工具，本次快照应只有 `lab-greeting==1.0.0`。rebuilt 应通过同样两项测试，证明依赖可重装，无须复制 A。

应用 requirements 是维护者的要求，snapshot 是某次实际结果；复杂工程还需记录 Python、平台、传递依赖与来源，freeze 不是跨平台完整锁文件。交付的是源码、依赖、包获取方式和测试命令，不是虚拟环境目录。

**constraints** 是允许版本的限制，不会主动要求安装包。下面同时要求“小于 2”和“等于 2.0.0”，预期冲突：

```bash
printf 'lab-greeting<2\n' > constraints.txt
a/Scripts/python.exe -m pip install --no-index --find-links wheelhouse -c constraints.txt lab-greeting==2.0.0
echo $?
a/Scripts/python.exe -m unittest discover -s app/tests -v
```

printf 写一行文本；`-c constraints.txt` 为这次解析提供限制。安装故意非零退出，报告冲突；随后 A 测试仍通过，确认没有升到 v2。恢复方法是停止本次不一致的升级，而不是去掉限制偷偷换版本。

## 8. 修改配置，证明文件作用域

pip 的选项还能来自配置文件。这里仅修改练习环境 A：

```bash
a/Scripts/python.exe -m pip config --site set global.timeout 30
a/Scripts/python.exe -m pip config --site get global.timeout
a/Scripts/python.exe -m pip config debug
a/Scripts/python.exe -m pip config --site unset global.timeout
```

`--site` 选择当前虚拟环境配置；global.timeout 中的 global 是配置段名，不表示写用户全局文件。set 写入、get 读取，预期为 30；debug 展示查找过的文件及状态，Windows 通常写入 a/pip.ini；unset 删除本节新增键。timeout 控制网络等待，不控制包版本，本节只证明配置来源，没有借网络超时测试它。

若结果不同，先排查 `PIP_CONFIG_FILE`、`PIP_TIMEOUT` 环境变量等覆盖来源，不修改用户或公司的镜像配置。[P03](../P03_配置依赖并重建环境.md)进一步解释配置优先级。

## 9. 修改源码：常规安装为何不变，可编辑安装为何变化

A 使用 wheel 安装副本，改 package_v1 源码不会自动改变 A。开发自己的包可用 **editable install（可编辑安装）**，让环境关联开发源码。

```bash
cp -R package_v1 edit-src
py -3.12 -m venv dev
dev/Scripts/python.exe -m pip install --no-index --find-links bootstrap setuptools==80.9.0
dev/Scripts/python.exe -m pip install --no-index --no-build-isolation -e ./edit-src
dev/Scripts/python.exe -c "import lab_greeting; print(lab_greeting.__file__)"
dev/Scripts/python.exe -m unittest discover -s app/tests -v
```

`-e` 选择可编辑模式，后端使用已准备的 setuptools。导入位置应在 edit-src/src，测试先通过。改元信息、入口命令或本地扩展时仍可能需要重新安装，不能推广成所有改动都无需构建。

打开副本 `edit-src/src/lab_greeting/__init__.py`，只把函数中的这一行：

```python
    return f"hello {name} from v1"
```

临时改成：

```python
    return f"hello {name} from broken"
```

这次故意注入错误，应用要求没有改变，不修改测试期望。

```bash
dev/Scripts/python.exe -m unittest discover -s app/tests -v
echo $?
a/Scripts/python.exe -m unittest discover -s app/tests -v
```

Dev 应两项失败，A 仍两项通过。每次命令都启动新 Python 进程，因此 Dev 会重新读取改过的源码；A 读的是自己的安装副本。将刚改的一行恢复成 from v1，再执行 Dev 的测试，必须回到 OK。

## 10. 重开终端、迁移与复练

新开 UCRT64 Bash，在仓库根执行：

```bash
cd build/learning-tools/venv-practice
rebuilt/Scripts/python.exe -m unittest discover -s app/tests -v
```

无需激活，仍应两项通过，排除“只在原窗口临时状态下有效”。Linux/macOS 将基础解释器改成已核对的 python3，Scripts/python.exe 改为 bin/python，激活路径改为 bin/activate；本轮实测仅覆盖 Windows 主线。

迁移到自己的工程时，复制 application 模板，替换业务、依赖和断言。例如嵌入式辅助工具可以测试固件头校验、串口帧解析或配置生成。新增一个 `greet("sensor")` 的断言后应为 3 项通过；参考写法是在测试类中新增方法并调用 `self.assertEqual(greet("sensor"), "hello sensor from v1")`。先解释该断言保护的行为，再添加测试。

自己的实验记录至少回答：A 不激活为何可用；pip check 成功为何仍有 FAIL；卸载 B 为何不影响 A；rebuilt 如何证明重建；Dev 与 A 为何读取不同副本。

重新练习在第 1 节换 venv-practice-02。清理前退出环境、离开练习目录并保存修改，再用文件管理器删除核对过的本次 venv-practice 目录，不删除根 .venv 或教材 labs。产物已被 Git 忽略，可复用的源码和测试才跟随仓库。

依据：[Python 3.12 venv](https://docs.python.org/3.12/library/venv.html)、[pip install](https://pip.pypa.io/en/stable/cli/pip_install/)、[unittest 测试发现](https://docs.python.org/3.12/library/unittest.html#test-discovery)。[维护者验证](../../../VALIDATION.md)与本页手动操作各有职责，不能用一个自动脚本的成功代替逐步理解。
