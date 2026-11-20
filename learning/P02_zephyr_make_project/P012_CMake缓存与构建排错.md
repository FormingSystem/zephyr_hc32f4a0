---
id: learning.zephyr.chapter-011
title: CMake缓存与构建排错
kind: engineering
status: maintained
domains: [zephyr, cmake, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第12章\_CMake缓存与构建排错

昨天构建成功，今天把模块移到新目录，配置输出却还在引用旧位置。第一次配置时，CMake 已经把部分选择写进构建目录的 `CMakeCache.txt`。要找出旧值从哪里来，先分清三个时刻：启动进程时有哪些输入，配置时采用了哪个值，生成后哪条编译命令实际引用它。

用 [P008 的首次构建](P008_选择应用与硬件目标并构建.md#section-8-6-1) 作对照。示例读取 `build/learning-tools/first-ucrt-zip`；其他单镜像路线使用各自的 `-B` 目录，sysbuild 从 `domains.yaml` 找对应域。本章的[缓存实验](reference/CMake缓存的设置与恢复实验.md)只改配置日志级别：先读原值，设置 `VERBOSE`，在下一次配置时省略该参数再查，最后恢复。若值仍在，便能把影响范围定位到这份构建目录。排查模块时，再沿[产物检查](#section-12-2-1)比较缓存、有效配置与编译数据库。

以下示例沿用同一份应用源码，比较复用构建目录和另建目录时，CMake 怎样处理 SDK、板目标和应用配置。

**复制命令：** [当前命令索引](commands/current/P012_CMake缓存与构建排错/README.md)。按正文选择分支，不把整个目录的命令依次执行。

<a id="input-lifetime"></a>

<a id="section-12-1"></a>

## 12.1\_配置怎样保存，接口怎样组合

先观察同一构建目录怎样保留输入，再区分临时变量、缓存和可复用预设。下面的小实验只改变一项，以便确定旧设置为什么仍然生效。

<a id="section-12-1-1"></a>

### 12.1.1\_终端变量、工程预设与构建缓存

现在才讨论范围，是因为已经知道 BOARD、SDK 根和模块列表各自交给谁。以固定 SDK 根为例，Bash 的 `export` 把值放进当前进程环境，后续启动的 CMake 可以读取；命令行 `-D` 把值交给某一个构建目录的 CMake 缓存；CMake 文件中的 `set` 默认创建普通变量。这三种容器互相独立。

| 选择方式 | 保存在哪里 | 对哪些操作有效 | 改变或退出的方法 |
| --- | --- | --- | --- |
| 当前 Bash `export` | 当前终端及后续子进程的环境 | 由这个终端启动、且会读取该环境的程序 | 当前终端 `unset` 或关闭；已经形成的构建缓存仍存在 |
| CMake `-D` | 对应 `-B` 目录的 `CMakeCache.txt` | 这个构建目录后续配置 | 对允许变更的项重传；换板/工具组合优先用新构建目录 |
| CMake `set` | 普通变量作用域；带 CACHE 时涉及缓存 | 当前执行的目录/函数等作用域 | 修改定义者；普通 set 不自动成为全局永久设置 |
| `CMakeUserPresets.json` | 应用旁由读者自行创建的用户文件 | 选择相应 `cmake --preset` 时 | 修改所选预设；存在文件时合并，不覆盖个人配置 |
| SDK 包注册 | 当前用户的 CMake 包位置记录 | 使用包搜索的工程 | SDK 移动后重新注册并核对实际发现结果 |

预设属于 CMake 功能，是保存参数组合的方式，不是另一套 Zephyr 工具链。`.venv` 解决 Python 包隔离，不能称为 SDK 的永久工程配置；本系列不修改自动生成的 activate 脚本来暗中固定 SDK。依据：[CMake 变量读取规则](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variables)（原件 `CMake 变量与作用域`）；[CMake 工程预设](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html)（原件 `CMakePresets.json / CMakeUserPresets.json`）；[SDK 输入与默认查找分支](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/FindZephyr-sdk.cmake#L44)（原件 `cmake/modules/FindZephyr-sdk.cmake`，第 44 行附近）。

例如，给一次配置传入 `-DCMAKE_MESSAGE_LOG_LEVEL:STRING=VERBOSE`，CMake 便把日志级别写进当前构建目录的 `CMakeCache.txt`。下一次配置沿用同一个 `-B`，即使省略该选项，仍会读到 `VERBOSE`。新建的构建目录有自己的缓存。要撤销这次修改，原先没有该项时用 `-U CMAKE_MESSAGE_LOG_LEVEL` 重新配置，原先有值则写回原值。[在同一构建目录设置、复查并恢复日志级别](reference/CMake缓存的设置与恢复实验.md)

<a id="section-12-1-2"></a>

### 12.1.2\_缓存与环境变量的读取顺序

CMake 的 `${名字}` 通常先找普通变量、再找缓存；`$ENV{名字}` 明确读进程环境。Zephyr 的辅助函数还能自行规定读取顺序。SDK 相关输入调用 `zephyr_get`；本系列普通单应用、不使用 snippets 的情况，相关标量按**缓存、环境、当前普通值**寻找已定义输入。

因此，第一次用 SDK-A 配置构建目录后，第二次只在终端 export SDK-B，旧缓存可能仍使 A 生效。这是同一构建目录在保留选择，不是“注册失败”。换工具组合时使用新的构建目录，可以避免关联编译器和库配置残留；不能仅修改一个缓存路径就假定全部状态同步。

还应区分 `ZEPHYR_SDK_INSTALL_DIR` 与 `Zephyr-sdk_DIR`：前者是 Zephyr 的 SDK 搜索位置输入，后者是 CMake 保存的 SDK 包配置目录。即使重新传了前者，有效的旧 `Zephyr-sdk_DIR` 仍可能先被 CMake 采用；`NO_DEFAULT_PATH` 只限制后续搜索范围，不会删除已有包缓存。前者还可以指向多版本父目录，所以“指定搜索位置”与“已验证选中某个 SDK”也要分开。换 SDK 时用新构建目录，并一起核对这两个值与 `CMAKE_C_COMPILER`，不通过盲删其他缓存项修复。具体读取者为 `cmake/modules/FindZephyr-sdk.cmake` 的包查找分支，以及 CMake 的 [`find_package` 配置模式](https://cmake.org/cmake/help/latest/command/find_package.html#config-mode-search-procedure)。

完整函数还考虑 sysbuild 与 snippets 作用域，不能把这个简化顺序说成所有 CMake 变量的通用规则。`ZEPHYR_BASE` 有自己的包入口分支；额外模块也不同：`EXTRA_ZEPHYR_MODULES` 与兼容名 `ZEPHYR_EXTRA_MODULES` 使用 MERGE 合并来源，所以只给空 `-D` 不一定清除环境里追加的路径。P014 的恢复分支分别处理旧环境和新构建目录。依据：[Zephyr 输入读取与优先级](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/extensions.cmake#L4088)（原件 `cmake/modules/extensions.cmake`，第 4088 行附近）；[模块输入与发现脚本调用](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/zephyr_module.cmake#L34)（原件 `cmake/modules/zephyr_module.cmake`，第 34 行附近）；[包入口 include_boilerplate](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/share/zephyr-package/cmake/ZephyrConfig.cmake#L28)（原件 `share/zephyr-package/cmake/ZephyrConfig.cmake`，第 28 行附近）。

<a id="interface-combinations"></a>

<a id="section-12-1-3"></a>

### 12.1.3\_按要改变的对象选择接口

| 本次要改变什么 | 使用或保留的接口 | 不应误做的事情 |
| --- | --- | --- |
| 编译已支持的官方板 | 选择应用和 BOARD，默认 SDK 与 west 模块可继续使用 | 为了表示“用 Zephyr”重复设置默认类型 |
| 多套 SDK 选择一套 | 新构建目录中指定目标 SDK 根，并核对包目录与编译器 | 把 SDK 根填成 TOOLCHAIN_ROOT，或忽略旧 Zephyr-sdk_DIR |
| 改用独立 GNU 编译器组件 | 选择 cross-compile 与程序前缀，核对目标库 | 把独立组件称作 Minimal SDK |
| 加一个 HAL 项目 | 下载后通过追加模块接口提供根路径 | 替换整份默认模块列表或直接伪造 MODULE_DIR |
| 增加树外板/SoC | 提供相应搜索根或模块 settings，并实现硬件文件 | 只换 BOARD 名称就宣称硬件存在 |
| 改应用功能或硬件属性 | 分别提供 Kconfig 片段或 overlay | 把 CONF_FILE 当布尔开关，或把 overlay 当 CMake 脚本 |
| 给库增加一个实现文件 | 执行到该 CMake 入口后，用目标/库函数加源码 | 只把文件复制进目录便期待自动构建 |

这张表的作用是让输入与工作相对应。正常选择一个已支持的 Cortex-M 板，通常不涉及自定义工具链规则；新增一个源码模块也不要求重写应用加载 Zephyr 的包入口。

<a id="section-12-1-4"></a>

### 12.1.4\_更大工程还有哪些扩展入口

`BOARD_ROOT`、`SOC_ROOT`、`DTS_ROOT` 扩展硬件描述查找范围；`MODULE_EXT_ROOT` 用于模块接入文件放在外部的位置；`TOOLCHAIN_ROOT` 扩展工具链接入规则。它们虽然都带 ROOT，所寻找的目录结构和读取者不同。

snippets 用于给构建添加命名的配置片段；sysbuild 在外层协调多个镜像，各镜像仍有自己的 Zephyr 配置与产物。初学单应用时先理解本章主线，遇到多镜像需求再进入 sysbuild，而不是在普通命令里预先堆上这些变量。配套的[构建接口与源码索引](reference/UCRT64构建故障与源码依据.md#section-12-3)列出这些入口。依据：[外部项目模块说明](https://docs.zephyrproject.org/latest/develop/modules.html)（原件 `doc/develop/modules.rst`，第 3 行附近）；[树外工具链设计说明](https://docs.zephyrproject.org/latest/develop/toolchains/custom_cmake.html)（原件 `doc/develop/toolchains/custom_cmake.rst`，第 3 行附近）；[配置片段组合入口](https://docs.zephyrproject.org/latest/build/snippets/index.html)（原件 `doc/build/snippets/index.rst`，第 3 行附近）；[多镜像构建入口](https://docs.zephyrproject.org/latest/build/sysbuild/index.html)（原件 `doc/build/sysbuild/index.rst`，第 3 行附近）。


<a id="section-12-2"></a>

## 12.2\_怎样证明工程采用了这些输入

输入被接受不等于固件用了预期源码。按配置、生成、编译和链接的顺序检查产物，才能把所填路径与最终结果对应起来。

<a id="section-12-2-1"></a>

### 12.2.1\_按阶段读产物

源码中的脚本说明机制，实际构建的产物说明本次选择。它们需要互相对应。

| 要回答的问题 | 在所选构建目录里看什么 | 能证明到哪一步 |
| --- | --- | --- |
| 选中了哪个应用、源码、板和 SDK | 配置日志及 `CMakeCache.txt` | 配置采用的入口与保存值；不代表实板运行成功 |
| 功能最终启用了什么 | `zephyr/.config` | Kconfig 计算结果 |
| 硬件描述合并后是什么 | `zephyr/zephyr.dts` | DTS/overlay 处理结果 |
| CMake 识别了哪些模块 | `zephyr_modules.txt` | 模块根与 CMake 入口记录；不代表每个文件都编译 |
| 某个 C 文件被安排怎样编译 | 生成阶段导出的 `compile_commands.json` | 编译器、CPU 参数、宏与头文件目录；不证明任务已经执行 |
| 最终有没有生成固件 | `zephyr/zephyr.elf` 和构建日志 | 构建完成；运行和烧录另验 |

这些都是**工具生成文件**，应在成功执行对应阶段后出现；第一次只读 P008 时没有它们是正常的，不需要提前手建。P008 的 8.5 已实际构建的读者可直接做 [first-ucrt-zip 自查](#cmake-result-check)；本册所有自查均以 first-ucrt-zip 为准。日志中的真实任务执行、生成阶段安排的编译命令和磁盘上保留的旧产物，应分别判断。

<a id="section-12-2-2"></a>

### 12.2.2\_AN386 构建目录

本章沿用 P008 的 `build/learning-tools/first-ucrt-zip`。继续使用下方 12.2.4 的只读命令核对，不混读 P014 的其他构建目录。缓存不存在或生成失败时先回 P008，不手工创建空文件。

<a id="section-12-2-3"></a>

### 12.2.3\_从构建记录定位输入

**下载了一个 HAL，目录里有 module.yml，为什么编译器仍找不到头文件？** 从报错的那一个 `.c` 出发，在 `compile_commands.json` 找它的编译命令。对于 `#include <vendor/foo.h>`，若磁盘上的文件是 `包根/include/vendor/foo.h`，编译器需要能从搜索目录 `包根/include` 拼出这个文件名。少了这个搜索目录，再查 `zephyr_modules.txt`：没有模块记录，先查发现路径；已有记录，则查模块构建规则是否在当前配置下把这个目录传给了编译目标。这样同一个错误信息就能区分两种原因。

**SDK 已注册，为什么还会用旧 SDK？** 注册提供包搜索候选；旧环境、所选预设或构建缓存可能明确约束了另一套位置。先看实际配置输入和保存范围，不要反复 reinstall 或为每个终端重新注册。

**从 MPS2 换到 HC32，为什么不能只改工具链变量？** 同一套 ARM 编译器能为两种芯片生成指令，却无法从指令集推出控制台接在哪个 USART。换板需要选择 HC32 的 SoC 支持，让板描述给出控制台节点，让匹配驱动以该节点的地址初始化 USART。若编译清单里仍是 MPS2 的 CMSDK UART、最终设备树里仍是 AN386 的硬件，更换 GCC 的安装目录不会改变这两个结果。[HC32 的完整接入实验](P014_HC32与外部源码模块接入.md#section-14-6)

<a id="cmake-result-check"></a>

### 12.2.4\_在本章构建目录完成自查与排错

现在把“缺组件”拆成可以核查的事实。磁盘上没有 CMSIS 原始文件时，返回当前清单的下载步骤；文件在磁盘上但模块记录没有它时，检查传入的模块集合；记录已经有它但编译计划缺少所需源码时，继续看 Kconfig 和 CMake 条件。换板后缺 UART 驱动则要检查新板的设备树和驱动支持，不能靠重装 CMSIS 解决。下面按这个顺序读取同一份产物。

以下两项检查只读同一次构建的产物。在已设置 `ZEPHYR_BASE` 的 UCRT64 终端中，默认读取 P008 的 `build/learning-tools/first-ucrt-zip`。要检查 P010 的结果，先将 `AN386_BUILD_DIR` 设为 `build/learning-tools/p010/west-an386` 或 `build/learning-tools/p010/cmake-an386`。

```bash
# UCRT64；从已设置的源码根读取本次构建的生成文件。
cd "$ZEPHYR_BASE"
build_dir="${AN386_BUILD_DIR:-build/learning-tools/first-ucrt-zip}"
# 只读工具生成文件；不存在时返回配置步骤，不创建空文件。
if test -f "$build_dir/CMakeCache.txt"; then
  # 源码、应用、板、生成器和 Python 的保存值。
  grep -E '^(CMAKE_HOME_DIRECTORY|CMAKE_GENERATOR|BOARD|BOARD_QUALIFIERS|ZEPHYR_BASE|Zephyr_DIR|Python3_EXECUTABLE):' \
    "$build_dir/CMakeCache.txt"
  # SDK 选择与配置阶段确定的 C 编译器。
  grep -E '^(ZEPHYR_TOOLCHAIN_VARIANT|ZEPHYR_SDK_INSTALL_DIR|Zephyr-sdk_DIR|CMAKE_C_COMPILER):' \
    "$build_dir/CMakeCache.txt"
else
  printf '%s\n' '尚无本章缓存，请核对所选输出目录并完成配置。'
fi
# CMSIS 记录是模块发现结果；这里不下载、不添加模块。
if test -f build/learning-tools/first-ucrt-zip/zephyr_modules.txt; then
  grep '"cmsis_6"' build/learning-tools/first-ucrt-zip/zephyr_modules.txt
else
  printf '%s\n' '尚无模块记录，请检查配置日志并返回 P006—P010。'
fi
```

本例应能关联出同一组选择：应用是 `samples/hello_world`，板是 `mps2/an386`，生成器是 Ninja，Python 指向项目 `.venv/Scripts/python.exe`，Zephyr 包入口位于当前源码根的 `share/zephyr-package/cmake`，SDK 根为实际选中的 SDK，`Zephyr-sdk_DIR` 指向该 SDK 的 `cmake` 包目录，C 编译器在它的 `gnu/arm-zephyr-eabi/bin` 下。本例缓存中 SDK 根的 Windows 路径为 `G:/zephyr_practice/zephyr-sdk-1.0.1`，读者使用其他有效位置时不必强行改成这个路径。BOARD 及限定项的保存形态可能随版本规范化，以板日志和相关记录共同核对。

`cmsis_6` 的模块记录应指向 P005 获取的源码根；第三列若保留 `${ZEPHYR_CMSIS_6_CMAKE_DIR}`，这是供 Zephyr 后续解析的外置接入入口表达式，不是目录丢失，也不是要求读者创建这个名字的文件。其后续读取链已在 11.3.2—11.3.3 展开。[检查模块和配置来源](commands/current/P012_CMake缓存与构建排错/complete/step-07.txt)。

再从生成的编译命令数据库只取 hello_world 的 main.c，避免在整份长 JSON 中反复搜索：

```bash
# UCRT64；从已设置的源码根读取本次构建的生成文件。
cd "$ZEPHYR_BASE"
build_dir="${AN386_BUILD_DIR:-build/learning-tools/first-ucrt-zip}"
source .venv/Scripts/activate
# 只读编译命令数据库；-X utf8 是 Python 的 UTF-8 模式，适配 UCRT64 输出。
# 不执行数据库中的命令，不修改源码或构建状态。
python -X utf8 - "$build_dir" <<'PY'
import sys
import json
from pathlib import Path

database = Path(sys.argv[1]) / 'compile_commands.json'
if not database.is_file():
    raise SystemExit('尚无编译命令数据库，请核对所选输出目录及其生成结果。')

target = Path('samples/hello_world/src/main.c').resolve()
for entry in json.loads(database.read_text(encoding='utf-8')):
    source = Path(entry['file'])
    if not source.is_absolute():
        source = Path(entry['directory']) / source
    if source.resolve() == target:
        print('源文件：', source)
        print('命令工作目录：', entry['directory'])
        print('生成阶段安排的编译命令：')
        print(entry.get('command') or json.dumps(entry['arguments'], ensure_ascii=False))
        break
else:
    raise SystemExit('未找到 hello_world 的 main.c，请核对当前应用与构建目录。')
PY
```

**对应 `compile_commands.json` 查询块的三项输出：** “源文件”来自 `file`；“命令工作目录”来自 `directory`；“生成阶段安排的编译命令”来自 `command`，或没有该字段时的 `arguments` 列表。这段 Python 只读取 CMake 生成的 JSON，不创建测试工程，也不更改应用。`-X utf8` 是 Python 自身的 UTF-8 模式，用于这一条读取命令的中文输出，不是 Zephyr 变量，也不需要修改 `.venv`。观察打印命令的编译器路径、`-mcpu`/`-mthumb`、CMSIS 的头文件目录和 main.c 输入路径。`file` 表示源文件，`directory` 表示执行该编译命令时的工作目录；数据库中的相对路径应结合该目录理解。

编译数据库在配置和生成成功时即可读取。要确认该命令确已执行，可用 `cmake --build 构建目录 --verbose` 查看实际构建日志；输入没有改变时，Ninja 可以直接复用已生成的目标文件。[从编译数据库追踪应用源文件](commands/current/P012_CMake缓存与构建排错/complete/step-08.txt)

失败时先定位停在哪个阶段，再回到对应输入。不要看到最后一行 build stopped 就只改编译器路径。

| 看到的现象 | 当前优先核对 | 返回哪一步 |
| --- | --- | --- |
| 找不到应用 CMakeLists.txt，或报源目录不对 | 当前目录与 -S；是否把 SDK 或整个 Zephyr 根误当应用 | [P008 8.1](P008_选择应用与硬件目标并构建.md#81_应用入口和板目标分别选择什么) 与 8.5 |
| 找不到 Zephyr 包 | Zephyr_DIR 是否指向当前源码的包入口；不要用 SDK 根替代 | [P008 8.1.1](P008_选择应用与硬件目标并构建.md#zephyr-package-export) 与 [P011 11.1.2](P011_Zephyr的CMake输入与依赖发现.md#section-11-1-2) |
| 找不到 Python、SDK 或 CMSIS | 配置日志中的实际路径、缓存和依赖文件；按缺失对象处理 | P003、P004 或 P005—P010 |
| 构建目录没有规则，或无法加载缓存 | 上一次配置是否成功；--build 是否指向同一个目录 | [P008 8.5](P008_选择应用与硬件目标并构建.md#85_windows-ucrt64-明确工具和路径边界) |
| 生成器不匹配，或修改板/编译器后状态混杂 | 是否复用了原来的 -B | [P008 8.7](P008_选择应用与硬件目标并构建.md#section-8-7) 与 [清理与重建实验](reference/CMake缓存的设置与恢复实验.md#section-12-1-1-5)，改用独立输出目录 |
| 配置完成，随后 C 文件编译或链接失败 | 第一处编译/链接诊断及对应任务的完整命令 | 本章 12.2.4 的 --verbose 检查；核对源码、头文件、库与功能配置 |
| 修改缓存后没有表现出预期效果 | 改的是配置日志还是编译日志；是否又被脚本、环境或预设覆盖 | [复查日志级别](reference/CMake缓存的设置与恢复实验.md#cache-step-3)及 12.1.2 |
| 没有重新编译，只提示 no work to do | 文件是否保存、是否是当前 -S 的文件、是否已被目标引用 | [P008 8.5](P008_选择应用与硬件目标并构建.md#85_windows-ucrt64-明确工具和路径边界)—8.7 |


<a id="section-12-3"></a>

## 12.3\_确认读取缓存的构建规则

以 SDK 为例，配置命令给出 `ZEPHYR_SDK_INSTALL_DIR`，Zephyr 的 `FindZephyr-sdk.cmake` 据此搜索 SDK。CMake 还会把找到的包配置目录保存在 `Zephyr-sdk_DIR` 中。若新终端里改过 SDK 路径，而构建仍使用旧编译器，先在这次输出目录的 `CMakeCache.txt` 中对照这两个值，再在 `compile_commands.json` 中确认实际编译器路径。在新输出目录配置同一应用，可以保留原有固件作比较。[SDK 查找规则](../../cmake/modules/FindZephyr-sdk.cmake)

## 12.4\_按失败阶段定位构建故障

下载工具返回 HTTP 407 时，源码包尚未取得，应检查代理认证。若 CMake 已进入配置阶段，但报告找不到 CMSIS 或 YAML 文件，应核对模块目录、实际运行的 Python 和报错中的文件名。若编译已经开始，Ninja 最后一行只能说明构建停止；找到失败的编译命令及其第一条诊断，才能判断缺的是头文件、编译参数还是实现。

[按原始诊断核对 UCRT64 的下载、路径和模块发现故障](reference/UCRT64构建故障与源码依据.md)

阅读导航：前一阶段：[P011_Zephyr的CMake输入与依赖发现](P011_Zephyr的CMake输入与依赖发现.md)；下一阶段：[P013_自定义源码模块与配置开关](P013_自定义源码模块与配置开关.md)。
