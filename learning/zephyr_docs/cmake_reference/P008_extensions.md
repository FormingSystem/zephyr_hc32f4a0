---
id: learning.zephyr-docs.cmake-reference.module.extensions
title: extensions：CMake扩展命令
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/extensions.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_extensions：CMake扩展命令

原文：[extensions](https://docs.zephyrproject.org/latest/build/cmake-ref/module/extensions.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:extensions"></a>
<a id="extensions"></a>

本模块提供 Zephyr 的 CMake 扩展命令（Extension Command）。Zephyr 应用、Zephyr 模块以及构建系统本身，通过这些命令描述要构建的内容。

许多命令有 `_ifdef` 和 `_ifndef` 变体，以 Kconfig 选项为第一个参数，使构建规则能够按条件生效，无须再包裹一个 `if()` 块。

本模块作为 `find_package(Zephyr)` 的一部分加载，因此下列所有命令都可以在任意 Zephyr 应用或模块的 `CMakeLists.txt` 中使用。

本章目录：

- [Zephyr专用扩展（Zephyr-aware Extensions）](#zephyr-aware-extensions)
- [Kconfig专用扩展（Kconfig-aware Extensions）](#kconfig-aware-extensions)
- [CMake通用扩展（CMake-generic Extensions）](#cmake-generic-extensions)
- [设备树扩展（Devicetree Extensions）](#devicetree-extensions)
- [Zephyr链接器函数（Linker Functions）](#zephyr-linker-functions)
- [函数辅助宏（Function Helper Macros）](#function-helper-macros)
- [可链接可加载扩展（Linkable Loadable Extensions，LLEXT）](#linkable-loadable-extensions-llext)

<a id="zephyr-aware-extensions"></a>

## 8.1\_Zephyr专用扩展（Zephyr-aware Extensions）

<a id="zephyr"></a>

### 8.1.1\_zephyr_*：全局库操作

下列方法修改名为 `zephyr` 的 CMake 库（Library）。`zephyr` 是一个通用汇集库，接收那些仅凭全部 Zephyr 源文件共用的包含路径、宏定义和其他编译选项就能构建的源文件。

例如：

```cmake
zephyr_sources(
  random_esp32.c
  utils.c
)
```

是以下写法的简写：

```cmake
target_sources(zephyr PRIVATE
  ${CMAKE_CURRENT_SOURCE_DIR}/random_esp32.c
  ${CMAKE_CURRENT_SOURCE_DIR}/utils.c
)
```

下面两个调用图（Call Graph）用于给出高层概览，有意作了简化，并不完整：

```text
zephyr_library_cc_option()
         |
         v
zephyr_library_compile_options()  -->  target_compile_options()
```

```text
zephyr_cc_option()           --->  target_cc_option()
                                        |
                                        v
zephyr_cc_option_fallback()  --->  target_cc_option_fallback()
                                        |
                                        v
zephyr_compile_options()     --->  target_compile_options()
```

**`zephyr_sources`**

<a id="command:zephyr-sources"></a>

`zephyr_sources(<sources>...)`

向 `zephyr` 库（Library）添加源文件。详见 `target_sources`。

**`zephyr_include_directories`**

<a id="command:zephyr-include-directories"></a>

`zephyr_include_directories(<dirs>...)`

向 `zephyr` 库添加包含目录（Include Directory）。详见 `target_include_directories`。

**`zephyr_system_include_directories`**

<a id="command:zephyr-system-include-directories"></a>

`zephyr_system_include_directories(<dirs>...)`

向 `zephyr` 库添加系统包含目录（System Include Directory）。详见 `target_include_directories`。

**`zephyr_compile_definitions`**

<a id="command:zephyr-compile-definitions"></a>

`zephyr_compile_definitions(<defs>...)`

向 `zephyr` 库添加编译宏定义（Compile Definition）。详见 `target_compile_definitions`。

**`zephyr_compile_options`**

<a id="command:zephyr-compile-options"></a>

`zephyr_compile_options(<options>...)`

向 `zephyr` 库添加编译选项（Compile Option）。详见 `target_compile_options`。

**`zephyr_link_libraries`**

<a id="command:zephyr-link-libraries"></a>

`zephyr_link_libraries(<item>...)`

向 `zephyr` 库添加链接库（Link Library）。详见 `target_link_libraries`。

**`zephyr_libc_link_libraries`**

<a id="command:zephyr-libc-link-libraries"></a>

`zephyr_libc_link_libraries(<item> ...)`

向 `zephyr` 库的 `LIBC_LINK_LIBRARIES` 属性添加链接库。

此函数允许子系统定义一些库，使其在链接命令中排在其他所有库和模块之后。使用 `libc`、`libgcc` 等工具链库（Toolchain Library）时，这很有用：这些库可能在处理 `lib` 目录时就被加入，早于任何模块库，因而可能无法用于解析模块中的符号（Symbol）。

**`zephyr_cc_option`**

<a id="command:zephyr-cc-option"></a>

`zephyr_cc_option(<option>...)`

向 `zephyr` 库添加编译器支持的选项。此函数逐一检查编译器是否支持各选项；支持时才将其加入 `zephyr` 库。

**`zephyr_cc_option_fallback`**

<a id="command:zephyr-cc-option-fallback"></a>

`zephyr_cc_option_fallback(<option1> <option2>)`

向 `zephyr` 库添加一个编译选项；第一个不受支持时，回退到第二个。

函数先检查编译器是否支持 `<option1>`，支持则添加它；否则检查 `<option2>`，并在支持时添加第二个选项。

**`zephyr_ld_options`**

<a id="command:zephyr-ld-options"></a>

`zephyr_ld_options(<options>...)`

向 `zephyr` 库添加链接器选项（Linker Option）。详见 `target_ld_options()`。

**`zephyr_get_include_directories_for_lang_as_string`**

<a id="command:zephyr-get-include-directories-for-lang-as-string"></a>

`zephyr_get_include_directories_for_lang_as_string(<lang> <var> [STRIP_PREFIX])`

以字符串（String）形式获取指定语言的包含目录，并写入变量 `<var>`。

`<lang>` 可以是 `C`、`CXX` 或 `ASM`。指定 `STRIP_PREFIX` 可从结果中省略前缀。

**`zephyr_get_system_include_directories_for_lang_as_string`**

<a id="command:zephyr-get-system-include-directories-for-lang-as-string"></a>

`zephyr_get_system_include_directories_for_lang_as_string(<lang> <var> [STRIP_PREFIX])`

以字符串（String）形式获取指定语言的系统包含目录，并写入变量 `<var>`。

`<lang>` 可以是 `C`、`CXX` 或 `ASM`。指定 `STRIP_PREFIX` 可从结果中省略前缀。

**`zephyr_get_compile_definitions_for_lang_as_string`**

<a id="command:zephyr-get-compile-definitions-for-lang-as-string"></a>

`zephyr_get_compile_definitions_for_lang_as_string(<lang> <var> [STRIP_PREFIX])`

以字符串（String）形式获取指定语言的编译宏定义，并写入变量 `<var>`。

`<lang>` 可以是 `C`、`CXX` 或 `ASM`。指定 `STRIP_PREFIX` 可从结果中省略前缀。

**`zephyr_get_compile_options_for_lang_as_string`**

<a id="command:zephyr-get-compile-options-for-lang-as-string"></a>

`zephyr_get_compile_options_for_lang_as_string(<lang> <var> [STRIP_PREFIX])`

以字符串（String）形式获取指定语言的编译选项，并写入变量 `<var>`。

`<lang>` 可以是 `C`、`CXX` 或 `ASM`。指定 `STRIP_PREFIX` 可从结果中省略前缀。

**`zephyr_get_include_directories_for_lang`**

<a id="command:zephyr-get-include-directories-for-lang"></a>

`zephyr_get_include_directories_for_lang(<lang> <var> [STRIP_PREFIX])`

以列表（List）形式获取指定语言的包含目录，并写入变量 `<var>`。

`<lang>` 可以是 `C`、`CXX` 或 `ASM`。指定 `STRIP_PREFIX` 可从结果中省略前缀。

**`zephyr_get_system_include_directories_for_lang`**

<a id="command:zephyr-get-system-include-directories-for-lang"></a>

`zephyr_get_system_include_directories_for_lang(<lang> <var> [STRIP_PREFIX])`

以列表（List）形式获取指定语言的系统包含目录，并写入变量 `<var>`。

`<lang>` 可以是 `C`、`CXX` 或 `ASM`。指定 `STRIP_PREFIX` 可从结果中省略前缀。

**`zephyr_get_compile_definitions_for_lang`**

<a id="command:zephyr-get-compile-definitions-for-lang"></a>

`zephyr_get_compile_definitions_for_lang(<lang> <var> [STRIP_PREFIX])`

以列表（List）形式获取指定语言的编译宏定义，并写入变量 `<var>`。

`<lang>` 可以是 `C`、`CXX` 或 `ASM`。指定 `STRIP_PREFIX` 可从结果中省略前缀。

**`zephyr_get_compile_options_for_lang`**

<a id="command:zephyr-get-compile-options-for-lang"></a>

`zephyr_get_compile_options_for_lang(<lang> <var> [STRIP_PREFIX])`

以列表（List）形式获取指定语言的编译选项，并写入变量 `<var>`。

`<lang>` 可以是 `C`、`CXX` 或 `ASM`。指定 `STRIP_PREFIX` 可从结果中省略前缀。

<a id="zephyr-library"></a>

### 8.1.2\_zephyr_library_*：当前库操作

Zephyr 库使用 CMake 的库概念，以及对 Zephyr 代码组织方式的一组约定，减少重复的样板代码（Boilerplate Code）。

可以通过 `zephyr_library()` 或 `zephyr_library_named()` 构造 Zephyr 库。构造函数创建 CMake 库，其名称可通过变量 `ZEPHYR_CURRENT_LIBRARY` 访问。

通常很少需要直接使用这个变量，因为 Zephyr 库提供了修改库的方法，其形式为 `zephyr_library_<target-function>`。这些方法封装 CMake 的 `target_*` 函数；底层函数文档见 `manual:cmake-commands(7)`。

为减少样板代码，这些方法调整了 CMake `target_*` API：默认采用 `PRIVATE`，目标默认是 `ZEPHYR_CURRENT_LIBRARY`。

通过 `zephyr_*` API 给出的选项与 `zephyr_library_*` API 冲突时，后者优先；也就是局部配置覆盖全局配置。

**`zephyr_library`**

<a id="command:zephyr-library"></a>

`zephyr_library()`

创建一个 Zephyr 库，其名称根据目录推导，并把 `ZEPHYR_CURRENT_LIBRARY` 变量设为推导出的名称。

**`zephyr_library_named`**

<a id="command:zephyr-library-named"></a>

`zephyr_library_named(<name>)`

以显式给出的名称创建 Zephyr 库，并把 `ZEPHYR_CURRENT_LIBRARY` 变量设为该名称。

**`zephyr_library_amend`**

<a id="command:zephyr-library-amend"></a>

`zephyr_library_amend([<dir>])`

为树外使用（Out-of-tree Usage）提供修改既有 Zephyr 库的功能。从 Zephyr 模块调用时，会查找 Zephyr 内定义的对应库。

`<dir>` 指定用于生成 Zephyr 库名称的树外基目录。当库的目录结构并非直接放在 `ZEPHYR_MODULE` 根目录，或模块集成文件位于 `MODULE_EXT_ROOT` 中时，可以使用此参数。

为确保修改的是正确的库，Zephyr 模块或 `<dir>` 基目录中的文件夹结构必须与 Zephyr 中的结构相对应。例如，要修改由 `ZEPHYR_BASE/drivers/entropy/CMakeLists.txt` 创建的库，可添加 `ZEPHYR_MODULE/drivers/entropy/CMakeLists.txt`，内容如下：

```cmake
zephyr_library_amend()
zephyr_library_sources(...)
```

修改 Zephyr 库时也可以使用生成器表达式（Generator Expression）。例如，需要将该库的文件夹公开为包含路径时，可以使用：

```cmake
zephyr_library_amend()
zephyr_library_include_directories($<TARGET_PROPERTY:SOURCE_DIR>)
```

更多目标属性（Target Property）和生成器表达式见 CMake 文档。

**`zephyr_library_sources`**

<a id="command:zephyr-library-sources"></a>

`zephyr_library_sources(<source> ...)`

向当前 Zephyr 库添加源文件（Source File）。

**`zephyr_library_include_directories`**

<a id="command:zephyr-library-include-directories"></a>

`zephyr_library_include_directories(<include_dir> ...)`

向当前 Zephyr 库添加包含目录（Include Directory）。

**`zephyr_library_link_libraries`**

<a id="command:zephyr-library-link-libraries"></a>

`zephyr_library_link_libraries(<item> ...)`

向当前 Zephyr 库添加链接库（Link Library）。

**`zephyr_library_compile_definitions`**

<a id="command:zephyr-library-compile-definitions"></a>

`zephyr_library_compile_definitions(<item> ...)`

向当前 Zephyr 库添加编译宏定义（Compile Definition）。

**`zephyr_library_compile_options`**

<a id="command:zephyr-library-compile-options"></a>

`zephyr_library_compile_options(<item> ...)`

向当前 Zephyr 库添加编译选项（Compile Option）。

**`zephyr_library_cc_option`**

<a id="command:zephyr-library-cc-option"></a>

`zephyr_library_cc_option(<option> ...)`

当 C 编译器支持给定编译选项时，将其添加到当前 Zephyr 库；不支持的选项会被忽略。

**`zephyr_library_add_dependencies`**

<a id="command:zephyr-library-add-dependencies"></a>

`zephyr_library_add_dependencies(<item> ...)`

向当前 Zephyr 库添加依赖（Dependency）。更多信息见 `add_dependencies()`。

**`zephyr_append_cmake_library`**

<a id="command:zephyr-append-cmake-library"></a>

`zephyr_append_cmake_library(<library>)`

将已有 CMake 库 `library` 加入 Zephyr CMake 库的全局列表。构造函数（Constructor）会自动完成这一操作；对于未使用 Zephyr 库构造函数的 CMake 库，必须显式调用本函数。

**`zephyr_library_import`**

<a id="command:zephyr-library-import"></a>

`zephyr_library_import(<library_name> <library_path>)`

将位于 `library_path` 的导入库（Imported Library）`library_name` 加入 Zephyr CMake 库的全局列表。

**`zephyr_library_app_memory`**

<a id="command:zephyr-library-app-memory"></a>

`zephyr_library_app_memory(<partition>)`

将当前 Zephyr 库放入应用内存分区（Application Memory Partition）。`partition` 参数是该库要放入的分区名称。

**注意：**确保已在源代码中使用 `K_APPMEM_PARTITION_DEFINE` 定义给定分区。

<a id="zephyr-interface-library"></a>

#### 8.1.2.1\_zephyr_interface_library_*：接口库

Zephyr 接口库（Interface Library）是 CMake `INTERFACE` 库的一层轻量封装。此抽象最重要的职责，是确保用户通过 Kconfig 启用某个库时，`app` 库能够访问该库的头文件。这样做，是因为用户启用库后，预期立即就能包含其头文件并调用函数。

当某些构建信息，例如包含目录、宏定义和编译选项，需要应用到一组 Zephyr 库，而 `app` 也可能属于这组库时，应使用 Zephyr 接口库。

Zephyr 库必须显式调用 `zephyr_library_link_libraries(<interface_library>)`，才能使用这些构建信息。为方便使用，`app` 被作为特例：每个 `interface_library` 应有对应的 Kconfig 选项 `CONFIG_APP_LINK_WITH_<interface_library>`，由它决定 `app` 是否链接该接口库。

与 `zephyr_library` API 类似，此 API 有构造函数，但没有对其他 CMake 目标函数的封装。

**`zephyr_interface_library_named`**

<a id="command:zephyr-interface-library-named"></a>

`zephyr_interface_library_named(<name>)`

以给定名称创建 Zephyr 接口库（Interface Library）。

<a id="generate-inc"></a>

### 8.1.3\_generate_inc_*：生成包含文件

需要生成一个可在构建时包含到应用中的文件时，可以使用这些函数。嵌入文件时，还可自动压缩。

使用示例见 `tests/application_development/gen_inc_file`。

**`generate_inc_file`**

<a id="command:generate-inc-file"></a>

`generate_inc_file(<source_file> <generated_file> ...)`

生成一个可在构建时包含到应用中的文件。

- `source_file`：要转换为十六进制的源文件。
- `generated_file`：生成的文件。
- `...`：额外参数传给 `file2hex.py`。

**`generate_inc_file_for_gen_target`**

<a id="command:generate-inc-file-for-gen-target"></a>

`generate_inc_file_for_gen_target(<target> <source_file> <generated_file> <gen_target> ...)`

生成一个可在构建时包含到应用中的文件，并让某个目标依赖于生成该文件的目标。

已有生成 `generated_file` 的目标时使用本函数；如果需要创建这样的目标，应使用 `generate_inc_file_for_target()`。

- `target`：依赖生成文件的目标。
- `source_file`：要转换为十六进制的源文件。
- `generated_file`：生成的文件。
- `gen_target`：生成 `generated_file` 的目标。
- `...`：额外参数传给 `file2hex.py`。

**`generate_inc_file_for_target`**

<a id="command:generate-inc-file-for-target"></a>

`generate_inc_file_for_target(<target> <source_file> <generated_file> ...)`

生成一个可在构建时包含到应用中的文件，并让某个目标依赖它。

本函数创建一个执行转换的目标，再让 `target` 依赖该目标，从而确保构建 `target` 中的任何内容之前，`generated_file` 已存在。

- `target`：依赖生成文件的目标。
- `source_file`：要转换为十六进制的源文件。
- `generated_file`：生成的文件。
- `...`：额外参数传给 `file2hex.py`。

<a id="board"></a>

### 8.1.4\_board_*：开发板扩展

本节提供与 Zephyr 开发板（Board）处理有关的扩展。

<a id="zephyr-board-runners"></a>

#### 8.1.4.1\_Zephyr开发板执行器（Board Runners）

开发板执行器（Board Runner）扩展函数允许构建系统控制 Zephyr 的开发板执行器。构建系统为受支持开发板提供烧录和调试目标；这些目标封装了 Zephyr west 工具中的 Python 执行器子包（Runner Subpackage）。

本节提供 CMake 与管理执行器的 Python 代码之间的衔接。

**`board_set_runner`**

<a id="command:board-set-runner"></a>

`board_set_runner(<type> <runner>)`

无条件设置开发板的执行器（Runner），预期从应用的 `CMakeLists.txt` 调用。

**注意：**在 `board.cmake` 中通常最好使用 `board_set_xxx_ifnset()`，这样用户仍能在 CMake 配置时或自己的应用 `CMakeLists.txt` 中设置执行器。

使用示例：

```cmake
board_set_runner(FLASH pyocd)
```

这会把开发板的烧录执行器设为 `pyocd`。一般来说，`type` 为 `FLASH`、`DEBUG`、`SIM` 或 `ROBOT`，`runner` 为执行器名称。

**`board_set_runner_ifnset`**

<a id="command:board-set-runner-ifnset"></a>

`board_set_runner_ifnset(<type> <runner>)`

此宏与 `board_set_runner()` 类似，但仅在当前未设置该执行器时才作修改。另见 `board_set_flasher_ifnset()` 和 `board_set_debugger_ifnset()`。

**`board_set_flasher`**

<a id="command:board-set-flasher"></a>

`board_set_flasher(<runner>)`

`board_set_runner(FLASH ${runner})` 的便捷宏。

**`board_set_debugger`**

<a id="command:board-set-debugger"></a>

`board_set_debugger(<runner>)`

`board_set_runner(DEBUG ${runner})` 的便捷宏。

**`board_set_flasher_ifnset`**

<a id="command:board-set-flasher-ifnset"></a>

`board_set_flasher_ifnset(<runner>)`

`board_set_runner_ifnset(FLASH ${runner})` 的便捷宏。

**`board_set_debugger_ifnset`**

<a id="command:board-set-debugger-ifnset"></a>

`board_set_debugger_ifnset(<runner>)`

`board_set_runner_ifnset(DEBUG ${runner})` 的便捷宏。

**`board_set_robot_runner_ifnset`**

<a id="command:board-set-robot-runner-ifnset"></a>

`board_set_robot_runner_ifnset(<runner>)`

`board_set_runner_ifnset(ROBOT ${runner})` 的便捷宏。

**`board_set_sim_runner_ifnset`**

<a id="command:board-set-sim-runner-ifnset"></a>

`board_set_sim_runner_ifnset(<runner>)`

`board_set_runner_ifnset(SIM ${runner})` 的便捷宏。

**`board_runner_args`**

<a id="command:board-runner-args"></a>

`board_runner_args(<runner> <args>...)`

供 `board.cmake` 和应用的 `CMakeLists.txt` 使用。

在 `board.cmake` 中的用法：

```cmake
board_runner_args(runner "--some-arg=val1" "--another-arg=val2")
```

构建系统随后确保用于创建执行器的命令行包含：

```text
--some-arg=val1 --another-arg=val2
```

在应用 `CMakeLists.txt` 中，确保所有 `board_runner_args()` 调用都位于名为 `app_set_runner_args()` 的宏中，并在调用 `find_package(Zephyr)` 之前定义该宏，如下所示：

```cmake
macro(app_set_runner_args)
  board_runner_args(runner "--some-app-setting=value")
endmacro()
```

构建系统检查这个宏是否存在；已定义时，在适当时机调用它。通过本函数显式提供的任何设置，都会覆盖构建系统给出的默认值。

**`board_set_rimage_target`**

<a id="command:board-set-rimage-target"></a>

`board_set_rimage_target(<target>)`

为当前开发板设置 rimage 目标（Target）。

<a id="zephyr-board-revision"></a>

#### 8.1.4.2\_Zephyr开发板修订版（Board Revision）

本节提供检查开发板修订版（Board Revision）的函数。

**`board_check_revision`**

<a id="command:board-check-revision-format"></a>

`board_check_revision(FORMAT <LETTER | NUMBER | MAJOR.MINOR.PATCH> [EXACT] [DEFAULT_REVISION <revision>] [HIGHEST_REVISION <revision>] [VALID_REVISIONS <revision> ...] )`

这是 Zephyr 开发板扩展函数，可在 `boards/board/revision.cmake` 中使用，将用户请求的修订版（Revision）与可用开发板修订版进行核对。

函数根据各参数，检查用户通过 `-DBOARD=board@revision` 提供的修订版。未指定 `EXACT` 时，将 Zephyr 构建系统变量 `ACTIVE_BOARD_REVISION` 设为选中的修订版。

`FORMAT <LETTER | NUMBER | MAJOR.MINOR.PATCH>` 指定修订版格式：

- `LETTER`：`A`—`Z` 中的单个字母。
- `NUMBER`：单个整数。
- `MAJOR.MINOR.PATCH`：用 `.` 分隔的三个数字，即 `x.y.z`。命令行可省略末尾的零，因此 `1.0.0 == 1.0 == 1`。

`OPTIONAL` 表示修订版指定符可选。未给出时使用基础开发板（Base Board）。同时给出 `EXACT` 和 `OPTIONAL` 时，可以不指定修订版；一旦指定，就必须满足 `EXACT` 要求。此参数与 `DEFAULT_REVISION` 互斥。

`EXACT` 要求修订版精确匹配。例如，可用修订版为 `0.1.0` 和 `0.3.0`，用户给出 `0.2.0`：有 `EXACT` 时报告错误；没有时选择最接近且更低的修订版，本例为 `0.1.0`。

`DEFAULT_REVISION` 指定用户未选择修订版时使用的默认值。如果未提供默认修订版，且命令行也未给出修订版，则向用户报告错误。

`HIGHEST_REVISION` 指定开发板允许的最高修订版，可防止较新的开发板搭配较旧的 Zephyr。例如，当前支持 `0.x.0`—`0.99.99` 和 `1.0.0`—`1.99.99`，预计现有实现不能用于 `2.0.0`，则可将此项设为 `1.99.99`；使用 `<board>@2.0.0` 或更高修订版时会报告错误。使用 `EXACT` 时不需要此项。

`VALID_REVISIONS` 给出此开发板的有效修订版列表。未提供时，开发板文件夹中每个形如 `board_revision.conf` 的 Kconfig 片段都作为有效修订版。

> 译注：原页签名未列出 `OPTIONAL`，但参数正文对它有完整说明；此处保留原签名及说明。上述无默认值时报错的规则，应与 `OPTIONAL` 允许省略修订版的分支一起阅读。

<a id="misc"></a>

### 8.1.5\_其他Zephyr扩展（Misc.）

**`pow2round`**

<a id="command:pow2round"></a>

`pow2round(<variable>)`

将数值向上舍入到下一个二的幂（Power of Two）。使用示例：

```cmake
set(test 2)
pow2round(test)
# test is still 2

set(test 5)
pow2round(test)
# test is now 8
```

**`zephyr_build_string`**

<a id="command:zephyr-build-string-outvar"></a>

`zephyr_build_string(outvar [BOARD board] [SHORT short_outvar] [BOARD_QUALIFIERS qualifiers] [BOARD_REVISION revision] [MERGE] [REVERSE])`

根据 `BOARD`、`BOARD_REVISION` 和 `BOARD_QUALIFIER` 创建构建字符串（Build String），以统一方式生成这些字符串。

提供 `MERGE` 时返回构建字符串列表，完整构建字符串位于第一项。完整顺序如下：

1. 规范化开发板目标的构建字符串，包含限定符（Qualifier）和修订版。
2. 在上一项基础上再去除开发板变体（Board Variant）。
3. 再去除 `cpuset`。
4. 再去除 `soc`。

若提供了 `REVISION`，或从系统范围设置取得了它，则每项除无修订版的条目外，还会增加一个带规范化修订版字符串的条目。

| 参数 | 含义 |
| --- | --- |
| `outvar` | 返回构建字符串的输出变量 |
| `BOARD board` | 用于生成构建字符串的开发板名称 |
| `SHORT short_outvar` | 返回缩短后构建字符串的输出变量 |
| `BOARD_QUALIFIERS qualifiers` | 要使用的开发板限定符 |
| `BOARD_REVISION revision` | 要使用的开发板修订版 |
| `MERGE` | 返回构建字符串列表，而非单个字符串 |
| `REVERSE` | 返回前反转列表 |

使用示例：

```cmake
zephyr_build_string(build_string BOARD alpha)
# Returns "alpha" in build_string

zephyr_build_string(build_string BOARD alpha
                                 BOARD_REVISION 1.0.0)
# Returns "alpha_1_0_0" in build_string

zephyr_build_string(build_string BOARD alpha
                                 BOARD_QUALIFIERS /soc/bar)
# Returns "alpha_soc_bar" in build_string

zephyr_build_string(build_string BOARD alpha
                                 BOARD_REVISION 1.0.0
                                 BOARD_QUALIFIERS /soc/bar
                                 MERGE)
# Returns list "alpha_soc_bar_1_0_0;alpha_soc_bar" in build_string

zephyr_build_string(build_string SHORT short_build_string
                                 BOARD alpha
                                 BOARD_REVISION 1.0.0
                                 BOARD_QUALIFIERS /soc/bar
                                 MERGE)
# Returns list "alpha_soc_bar_1_0_0;alpha_soc_bar" in build_string
# Returns list "alpha_bar_1_0_0;alpha_bar" in short_build_string

zephyr_build_string(build_string BOARD_QUALIFIERS /soc/bar/foo)
# Returns "soc_bar_foo" in build_string
```

> 译注：原文概述写作 `BOARD_QUALIFIER` 和 `REVISION`，而调用签名及参数表使用 `BOARD_QUALIFIERS` 和 `BOARD_REVISION`；调用时按签名的参数名填写。

> 源码核对译注：2026-10-14读取的[官方main实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/cmake/modules/extensions.cmake)与本页部分说明存在差异。`SHORT`分支实际读取外层变量`BOARD_QUALIFIERS`，而不是解析后的同名调用参数；独立运行上述短名称示例、且未定义外层变量时，返回`alpha_1_0_0;alpha`。将外层变量设为`/soc/bar`后，才得到原示例的`alpha_bar_1_0_0;alpha_bar`。此外，当前`MERGE`实现只补充去修订版的条目，并未逐级移除变体、cpuset和SoC；对`/soc/bar/foo`、修订版`1.0.0`，实际返回`alpha_soc_bar_foo_1_0_0;alpha_soc_bar_foo`。这些差异已用该次读取的官方函数复现，原示例和原说明保留供对照；`main`会变化，读取源码的摘要见来源记录。

**`zephyr_syscall_include_directories`**

<a id="command:zephyr-syscall-include-directories"></a>

`zephyr_syscall_include_directories(<directories>...)`

向传给系统调用生成器（Syscall Generator）的包含列表添加一个或多个目录。`<directories>...` 为要添加的目录。

**`zephyr_syscall_header`**

<a id="command:zephyr-syscall-header"></a>

`zephyr_syscall_header(<headers>...)`

向传给系统调用生成器（Syscall Generator）的列表添加一个或多个头文件。`<headers>...` 为要添加的头文件。

**`zephyr_syscall_header_ifdef`**

<a id="command:zephyr-syscall-header-ifdef-feature-toggle"></a>

`zephyr_syscall_header_ifdef(feature_toggle <headers>...)`

当 `feature_toggle` 为真时，向传给系统调用生成器（Syscall Generator）的列表添加一个或多个头文件。

- `feature_toggle`：要检查的布尔变量名称。
- `<headers>...`：要添加的一个或多个头文件。

**`zephyr_blobs_verify`**

<a id="command:zephyr-blobs-verify"></a>

`zephyr_blobs_verify(<MODULE module | FILES file [files...]> [REQUIRED])`

验证使用 west 获取的二进制资料（Blob）。如果 SHA-256 校验和（Checksum）不正确，打印警告或致命错误消息，级别由 `REQUIRED` 标志决定。

- `MODULE module`：验证给定模块的全部 Blob。
- `FILES file [files...]`：验证指定文件。
- `REQUIRED`：指定时，验证失败会产生致命错误；否则打印警告。

使用示例：

```cmake
# Verify all blobs in my_module and fail on error
zephyr_blobs_verify(MODULE my_module REQUIRED)

# Verify a single file and print on error
zephyr_blobs_verify(FILES img/file.bin)
```

<a id="kconfig-aware-extensions"></a>

## 8.2\_Kconfig专用扩展（Kconfig-aware Extensions）

Kconfig 是为 Linux 内核开发的配置语言。以下函数将 CMake 与 Kconfig 集成。

<a id="id1"></a>

### 8.2.1\_其他Kconfig扩展（Misc）

**`import_kconfig`**

<a id="command:import-kconfig-prefix-kconfig-fragment"></a>

`import_kconfig(prefix kconfig_fragment [keys] [TARGET target])`

解析 Kconfig 片段（通常扩展名为 `.config`），将其中以 `prefix` 开头的全部符号引入 CMake 命名空间（Namespace）。若给出输出变量 `keys`，则把所有创建的变量名称列入其中。

- `prefix`：Kconfig 片段中设置项的符号前缀。
- `kconfig_fragment`：配置片段文件的绝对路径（Absolute Path）。
- `keys`：输出变量，填入从 Kconfig 片段加载的变量名称。
- `TARGET`：将全部符号设置到 `target`，而不是加入 CMake 命名空间。

<a id="cmake-generic-extensions"></a>

## 8.3\_CMake通用扩展（CMake-generic Extensions）

这些函数对 CMake API 的扩展不局限于 Zephyr；主要用于绕过 CMake 语言的限制，使构建脚本更简洁。

**`add_subdirectory_ifdef`**

<a id="command:add_subdirectory_ifdef"></a>

`add_subdirectory_ifdef`

当 `feature_toggle` 启用时，将子目录加入构建。

<a id="debugging-cmake"></a>

### 8.3.1\_调试CMake（Debugging CMake）

**`print`**

<a id="command:print-arg"></a>

`print(arg)`

打印变量的值。使用示例：

```cmake
print(BOARD)
# will print: "BOARD: nrf52dk"
```

**`assert`**

<a id="command:assert-test-comment"></a>

`assert(test comment)`

断言（Assert）条件为真。若第一个表达式为假，此宏产生致命错误并打印错误消息。

- `test`：要检查的布尔表达式。
- `comment`：断言失败时打印的错误消息。

使用示例：

```cmake
assert(ZEPHYR_TOOLCHAIN_VARIANT "ZEPHYR_TOOLCHAIN_VARIANT not set.")
```

**`assert_not`**

<a id="command:assert-not-test-comment"></a>

`assert_not(test comment)`

断言（Assert）条件为假。若第一个表达式为真，此宏产生致命错误并打印错误消息。

- `test`：要检查的布尔表达式。
- `comment`：断言失败时打印的错误消息。

使用示例：

```cmake
assert_not(OBSOLETE_VAR "OBSOLETE_VAR has been removed; use NEW_VAR instead")
```

**`assert_exists`**

<a id="command:assert-exists-var"></a>

`assert_exists(var)`

断言文件或目录存在。如果变量所指向的文件或目录不存在，此宏产生致命错误。

`var` 为保存待检查路径的变量名称。使用示例：

```cmake
assert_exists(CMAKE_READELF)
```

<a id="file-system-management"></a>

### 8.3.2\_文件系统管理（File System Management）

**`generate_unique_target_name_from_filename`**

<a id="command:generate-unique-target-name-from-filename-filename-target-name"></a>

`generate_unique_target_name_from_filename(filename target_name)`

根据文件名生成唯一目标名称（Unique Target Name）。

- `filename`：据此生成唯一名称的文件名。
- `target_name`：保存生成目标名称的变量名称。

**`zephyr_file`**

<a id="command:zephyr-file-application-root"></a>

`zephyr_file(APPLICATION_ROOT <path> [BASE_DIR <base-dir>])`

<a id="command:zephyr-file-conf-files"></a>

`zephyr_file(CONF_FILES <paths> [DTS <list>] [KCONF <list>] [DEFCONF <list>] [BOARD <board> [BOARD_REVISION <revision>] | NAMES <name> ...] [SUFFIX <suffix>] [REQUIRED])`

这是 Zephyr 对文件操作函数的扩展，当前支持以下模式。

**`APPLICATION_ROOT`：**检查所给变量中的全部路径。对于通过 `-D<path>=<val>` 定义的路径，以 `APPLICATION_SOURCE_DIR` 为基准转换为绝对路径；遇到未由用户通过 `-D<path>` 指定的相对路径时，报告错误。返回更新后的绝对路径列表。

`BASE_DIR <base-dir>`：改为相对于 `<base-dir>` 转换路径，而不使用 `APPLICATION_SOURCE_DIR`。

**`CONF_FILES`：**在路径列表中查找全部配置文件，并以列表返回。若 `paths` 为空，不返回配置文件。配置文件类别如下：

- `DTS`：设备树覆盖文件（Devicetree Overlay File），扩展名 `.overlay`。
- `Kconfig`：配置片段（Configuration Fragment），扩展名 `.conf`。
- `defconfig`：默认配置文件，后缀 `_defconfig`。

配置文件搜索返回当前开发板已存在的配置文件。`CONF_FILES` 接受以下额外参数：

- `BOARD <board>`：查找指定开发板的配置文件。
- `BOARD_REVISION <revision>`：查找指定开发板修订版的配置文件，要求同时指定 `BOARD`。若未给出开发板，且没有指定 `NAMES`，则使用当前 `BOARD` 和 `BOARD_REVISION`。
- `NAMES <name1> [name2] ...`：要查找的文件名列表，替代根据开发板设置生成文件名的方式。仅将 `<paths>` 中找到的第一个匹配项返回到 `<list>`。
- `DTS <list>`：将 `<path>` 中的 DTS 覆盖文件追加到此列表。
- `KCONF <list>`：将 `<path>` 中的 Kconfig 片段文件追加到此列表。
- `DEFCONF <list>`：将 `<path>` 中的 `_defconfig` 文件追加到此列表。
- `SUFFIX <name>`：优先查找带此后缀的名称，找不到时回退到默认名称。例如，`SUFFIX fish` 优先使用找到的 `<file>_fish.conf`，否则使用 `<file>.conf`。
- `REQUIRED`：要求 `DTS` 或 `KCONF` 指定的 `<list>` 至少包含一个元素，否则报告错误。

**`zephyr_file_copy`**

<a id="command:zephyr-file-copy"></a>

`zephyr_file_copy(<oldname> <newname> [ONLY_IF_DIFFERENT])`

这是 Zephyr 的文件复制扩展。

**已弃用（Deprecated）：**此函数只因 CMake 3.20 不支持 `file(COPY_FILE...)` 而存在；应改为直接调用 `file(COPY_FILE ...)`。

- `oldname`：旧文件名。
- `newname`：新文件名。
- `ONLY_IF_DIFFERENT`：仅在文件不同时复制。

**`zephyr_file_suffix`**

<a id="command:zephyr-file-suffix"></a>

`zephyr_file_suffix(<filename> SUFFIX <suffix>)`

若带指定后缀的文件存在，用它更新文件名。

此函数检查给定的文件名或文件名列表，判断是否存在带 `_<suffix>` 扩展的文件；若存在，则用新路径更新所给变量或列表。

- `<filename>`：保存绝对路径文件名的变量，可以是单个值或列表。
- `<suffix>`：要检查并追加到给定文件名末尾的后缀。

返回更新后的绝对路径变量。

<a id="others"></a>

### 8.3.3\_其他功能（Others）

**`zephyr_string`**

<a id="command:zephyr-string-escape"></a>

`zephyr_string(ESCAPE <out-var> <input> ...)`

<a id="command:zephyr-string-sanitize"></a>

`zephyr_string(SANITIZE <out-var> <input> ...)`

<a id="command:zephyr-string-sanitize-toupper"></a>

`zephyr_string(SANITIZE TOUPPER <out-var> <input> ...)`

这是 Zephyr 对 CMake `string` 函数的扩展，为 `<mode>` 提供以下额外操作。

**`ESCAPE`：**在适当位置添加转义字符 `\`，确保 CMake 将输入参数的每个字符都视为字面量（Literal）。这适用于处理字符串中的 Windows 路径分隔符，或希望将 `\n` 写作原文字面字符串而不是单个换行的情况。原文将后一种字符串称为“四个字符”。在一个字符串的生命周期内，此操作必须恰好进行一次；否则，已有转义字符会被视为字面量并再次转义。

**`SANITIZE`：**确保输出字符串不含特殊字符。`-`、`+`、`=`、`$` 等特殊字符转换为下划线 `_`；多个参数会拼接起来。

**`SANITIZE TOUPPER`：**同样把 `-`、`+`、`=`、`$` 等特殊字符转换为 `_`，并拼接多个参数；规范化后的字符串以全大写（Upper Case）形式返回。

更新后的字符串返回到 `<out-var>`。

> 译注：显示为 `\n` 的字面文本由反斜杠和字母 n 两个字符组成；“四个字符”是原页文字，不应据此计算实际字符串长度。转义层数还取决于字符串出现的位置。

**`zephyr_list`**

<a id="command:zephyr-list-transform"></a>

`zephyr_list(TRANSFORM <list> <ACTION> [OUTPUT_VARIABLE <output variable>])`

这是 Zephyr 的列表函数扩展。与 CMake 的 `list(TRANSFORM ...)` 类似，它为当前及未来与 Zephyr 有关的列表处理扩展提供统一位置。

- `<ACTION>`：当前必须为 `NORMALIZE_PATHS`。先对列表内容进行 `configure_file` 转换，再把参数列表 `<list>` 转为使用 CMake 路径名、以 `;` 分隔的列表。输入列表可以用空白或分号分隔。
- `OUTPUT_VARIABLE`：默认原地保存结果；可用此参数指定另一个保存结果的变量。

**`zephyr_get`**

<a id="command:zephyr-get"></a>

`zephyr_get(<variable> [MERGE [REVERSE]] [SYSBUILD [LOCAL|GLOBAL]] [VAR <var1> ...])`

将 `<variable>` 的值返回为同名的局部作用域（Local Scope）变量。提供 `MERGE` 时，返回找到的各项组成的列表。

同时提供 `MERGE` 和 `REVERSE` 时，在返回前反转列表。反转发生在返回前，因此不会改变构造列表时采用的优先级顺序。

`VAR` 既可用于把结果保存到不同名称的变量，也可用于查找多个变量的值：

```cmake
zephyr_get(FOO VAR FOO_A FOO_B)
zephyr_get(FOO MERGE VAR FOO_A FOO_B)
```

`zephyr_get()` 为构建设置提供统一的读取方式；设置可以来自 Sysbuild、`CMakeLists.txt`、CMake 缓存或环境。

同一变量在多个作用域定义时，优先级由高到低为：

1. 使用 Sysbuild 时，由 Sysbuild 定义的值。它既可为全局，也可局部属于某个镜像。例如，`BOARD` 是全局 Sysbuild 缓存变量；`blinky_BOARD` 则仅属于 `blinky` 镜像。未指定 Sysbuild 作用域时，默认 `GLOBAL`。使用 `MERGE` 时，`SYSBUILD GLOBAL` 会取得局部和全局两个作用域的变量；若两者都存在，按局部、全局的顺序排列。
2. CMake 缓存：通过 `-D<var>=<value>` 或 `set(<var> <val> CACHE ...)` 设置。
3. 环境变量（Environment Variable）。
4. 在 `find_package(Zephyr)` 之前，于 `CMakeLists.txt` 中设置的局部值。

例如，环境中已经设置 `ZEPHYR_TOOLCHAIN_VARIANT`，又通过 `-DZEPHYR_TOOLCHAIN_VARIANT=<val>` 在 CMake 缓存中覆盖它，则返回缓存中的值。

**`zephyr_create_scope`**

<a id="command:zephyr-create-scope"></a>

`zephyr_create_scope(<scope>)`

创建用于保存作用域变量的新作用域（Scope）。`<scope>` 是新作用域名称。

**`zephyr_scope_exists`**

<a id="command:zephyr-scope-exists"></a>

`zephyr_scope_exists(<result> <scope>)`

检查 `<scope>` 是否存在。

- `<result>`：保存结果的变量；作用域存在时为 `TRUE`，否则为 `FALSE`。
- `<scope>`：作用域名称。

**`zephyr_get_scoped`**

<a id="command:zephyr-get-scoped"></a>

`zephyr_get_scoped(<output> <scope> <var>)`

取得特定 `<scope>` 中 `<var>` 的当前值；该值先前由 `zephyr_set()` 定义。结果存入 `<output>`。

- `<output>`：保存值的变量。
- `<scope>`：查找变量的作用域。
- `<var>`：要在此作用域中查找的名称。

**`zephyr_set`**

<a id="command:zephyr-set"></a>

`zephyr_set(<variable> <value> SCOPE <scope> [APPEND])`

这是 Zephyr 对 CMake `set` 的扩展，允许在特定作用域设置变量。同一变量在多个作用域设置时，后续 `zephyr_get()` 调用会使用作用域处理优先级。

- `<variable>`：变量名称。
- `<value>`：变量值；多个值形成列表，`SCOPE` 参数标记值列表结束。
- `SCOPE <scope>`：变量所属作用域名称。
- `APPEND`：向 `<scope>` 中已有变量追加值。

**`zephyr_check_cache`**

<a id="command:zephyr-check-cache"></a>

`zephyr_check_cache(<variable> [REQUIRED] [WATCH])`

检查当前 CMake 缓存中的 `<variable>`，若其值正被修改，则警告用户。这可防止用户意外尝试更改 `BOARD`、`SHIELD` 等 Zephyr 构建变量。

- `<variable>`：要检查和设置的变量名称，例如 `BOARD`。
- `REQUIRED`：可选标志；指定时，未设置 `<variable>` 会被视为错误。
- `WATCH`：可选标志；指定时监视该变量，若后续发生修改则打印警告。

`<variable>` 可以来自三个位置，优先级从高到低为：CMake 命令行参数 `-D<variable>`、环境变量，以及工程 `CMakeLists.txt` 中 `find_package(Zephyr)` 之前的设置。

第一次调用 CMake 时定义的值，将以 `CACHED_<variable>` 保存到 CMake 缓存。这样，Zephyr 构建系统便能检测用户何时重新配置了需要保持原值的变量（Sticky Variable）。

若始终使用同一来源且不混用，用户可以不必考虑这些优先级规则，例如始终在命令行指定 `-D<variable>=`、始终设置环境变量 `<variable>`，或始终在 `CMakeLists.txt` 中写 `set(<variable> foo)`。

后续 Zephyr CMake 代码通过变量 `<variable>` 访问所选值。如果用户尝试将其改为新值，系统打印警告，并使用优先级更高的旧缓存值 `CACHED_<variable>`。警告同时告知用户：要更改此变量，必须清理构建目录。

**`zephyr_get_targets`**

<a id="command:zephyr-get-targets"></a>

`zephyr_get_targets(<directory> <types> <targets>)`

获取给定目录及其子目录中的构建目标。

函数从 `<directory>` 开始遍历构建树（Build Tree），读取各目录的 `BUILDSYSTEM_TARGETS`，返回类型与 `<types>` 列表匹配的目标。例如，类型可以是 `OBJECT_LIBRARY`、`STATIC_LIBRARY`、`INTERFACE_LIBRARY` 或 `UTILITY`。

符合要求的目标列表返回到 `<targets>`。

**`target_byproducts`**

<a id="command:target-byproducts-target"></a>

`target_byproducts(TARGET <target> BYPRODUCTS <file> ...)`

指定目标会产生的额外构建副产物（Byproduct）。

本函数允许为 `add_executable` 创建的目标补充 `BYPRODUCTS`。链接器在链接可执行文件时，可能产生映射文件（Map File）等额外文件，而构建系统并不知道这些文件。此函数提供了简便的描述方式。

- `TARGET <target>`：要添加副产物的目标。
- `BYPRODUCTS <file> ...`：目标产生的副产物列表。

**`topological_sort`**

<a id="command:topological-sort-targets"></a>

`topological_sort(TARGETS <target> ... PROPERTY_NAME <property> RESULT <out-variable>)`

使用表示目标依赖的特定 `<property>`，对 CMake 目标进行拓扑排序（Topological Sort）。若所给依赖无法满足，例如包含环，则产生致命错误。

- `TARGETS <target> ...`：目标名称列表。
- `PROPERTY_NAME <property>`：排序使用的目标属性名称。对于 `TARGETS` 中每个目标，该属性必须包含一个列表，可以为空，列出此目标为特定用途所依赖的其他目标。列表不能包含未出现在 `TARGETS` 中的目标。
- `RESULT <out-variable>`：输出变量，返回拓扑排序后的目标名称列表。

**`build_info`**

<a id="command:build-info"></a>

`build_info(<tag>... VALUE <value>...)`

将与当前构建有关、可用于信息交换的构建信息写入 `build_info.yml` 文件。

使用示例：

```cmake
# This will update the 'devicetree.files' key in the build info yaml with the list of files
# file1.dts, file2.dts, file3.dts
build_info(devicetree files VALUE file1.dts file2.dts file3.dts)
```

```cmake
# This will place the vendor specific 'foo' key with value 'bar' in the vendor-specific
# section of the build info file.
build_info(vendor-specific foo VALUE bar)
```

- `<tag>...`：构建信息支持的预定义有效 CMake 键，或厂商专用键。有效标签见 `scripts/schemas/build-schema.yaml` 的 `cmake` 部分。
- `VALUE <value>...`：写入 `build_info.yml` 的值。
- `PATH <path>...`：写入 `build_info.yml` 的路径；全部转换为 CMake 风格。若无需转换，例如已经确保路径为 CMake 风格，也可以使用 `VALUE`。

<a id="devicetree-extensions"></a>

## 8.4\_设备树扩展（Devicetree Extensions）

<a id="dt"></a>

### 8.4.1\_dt_*：读取设备树

下列方法用于在 CMake 中取得设备树（Devicetree，DT）信息。

注意事项：

- 在 CMake 中通过节点路径引用节点，因此不存在类似 C 语言 `devicetree.h` API 中用于取得节点标识符的 `dt_path(...)` 函数。
- 与 C API 的另一个区别是，这些函数通常允许在路径开头使用别名，以替代对应节点的完整路径；各函数的使用说明会明确这一点。
- 这些方法也可供 Sysbuild 使用。要读取某个 `<image>` 的设备树信息，必须在该镜像的 CMake 配置步骤之后调用 `dt_*`，并提供 `TARGET <image>` 参数。

**`dt_nodelabel`**

<a id="command:dt-nodelabel"></a>

`dt_nodelabel(<var> NODELABEL <label> [REQUIRED] [TARGET <target>])`

获取节点标签（Node Label）为 `<label>` 的节点路径。路径返回到 `<var>`；节点不存在时，`<var>` 未定义。

- `<var>`：保存节点路径的返回变量。
- `NODELABEL <label>`：节点标签。
- `REQUIRED`：找不到节点标签时，产生致命错误。
- `TARGET <target>`：可选，指定从哪个目标取得设备树信息。

设备树片段示例：

```dts
/ {
   soc {
       nvic: interrupt-controller@e000e100  { ... };
   };
};
```

使用示例：

```cmake
# Sets 'nvic_path' to "/soc/interrupt-controller@e000e100"
dt_nodelabel(nvic_path NODELABEL "nvic")
```

**`dt_alias`**

<a id="command:dt-alias"></a>

`dt_alias(<var> PROPERTY <prop> [REQUIRED] [TARGET <target>])`

获取 `/aliases` 节点属性所对应的节点路径。路径返回到 `<var>`；别名（Alias）不存在时，变量保持未定义。

- `<var>`：保存节点路径的返回变量。
- `PROPERTY <prop>`：要检查的别名。
- `REQUIRED`：找不到别名时，产生致命错误。
- `TARGET <target>`：可选，指定从哪个目标取得设备树信息。

使用示例：

```cmake
# The full path to the 'led0' alias is returned in 'path'.
dt_alias(path PROPERTY "led0")

# The variable 'path' will be left undefined for a nonexistent
# alias "does-not-exist".
dt_alias(path PROPERTY "does-not-exist")
```

**`dt_node_exists`**

<a id="command:dt-node-exists"></a>

`dt_node_exists(<var> PATH <path> [TARGET <target>])`

检查设备树中是否存在路径为 `<path>` 的节点。`<path>` 可以是节点的绝对路径，例如 `/foo/bar`；节点别名，例如 `my-alias`；或节点别名后接子节点路径，例如 `my-alias/child-node`。

检查结果以 `TRUE` 或 `FALSE` 返回到 `<var>`。

- `<var>`：保存检查结果的返回变量。
- `PATH <path>`：节点路径。
- `TARGET <target>`：可选，指定从哪个目标取得设备树信息。

**`dt_node_has_status`**

<a id="command:dt-node-has-status"></a>

`dt_node_has_status(<var> PATH <path> STATUS <status> [TARGET <target>])`

检查 `<path>` 是否指向设备树中存在、且 `status` 属性与 `<status>` 参数匹配的节点。缺失 `status` 或状态为 `ok` 时，按 `okay` 处理。

`<path>` 可以是节点的绝对路径 `/foo/bar`、节点别名 `my-alias`，或别名后接子节点路径 `my-alias/child-node`。

检查结果以 `TRUE` 或 `FALSE` 返回到 `<var>`。

- `<var>`：保存检查结果的返回变量。
- `PATH <path>`：节点路径。
- `STATUS <status>`：要检查的状态。
- `TARGET <target>`：可选，指定从哪个目标取得设备树信息。

**`dt_prop`**

<a id="command:dt-prop"></a>

`dt_prop(<var> PATH <path> PROPERTY <prop> [INDEX <idx>] [REQUIRED] [TARGET <target>])`

获取设备树属性（Property）的值，返回到 `<var>`。

`<path>` 可以是节点的绝对路径 `/foo/bar`、节点别名 `my-alias`，或别名后接子节点路径 `my-alias/child-node`。

目前只支持以下设备树绑定类型：`string`、`int`、`boolean`、`array`、`uint8-array`、`string-array` 和 `path`。

对于数组属性，包括 `uint8-array` 和 `string-array`，未给出 `INDEX` 时，以 CMake 列表返回整个数组；给出时，只返回索引 `<idx>` 处的数组元素。

如果节点存在，且具有上述类型之一的 `<prop>` 属性，则将属性值返回到 `<var>`；否则 `<var>` 未定义。

- `<var>`：保存属性值的返回变量。
- `PATH <path>`：节点路径。
- `PROPERTY <prop>`：要返回其值的属性，名称与 DTS 源文件中的写法相同。
- `INDEX <idx>`：取得数组属性中某个值时使用的可选索引。
- `REQUIRED`：找不到属性时，产生致命错误。
- `TARGET <target>`：可选，指定从哪个目标取得设备树信息。

要在使用属性前检查它是否定义，可对返回变量 `<var>` 使用 `DEFINED`：

```cmake
dt_prop(reserved_ranges PATH "/soc/gpio@deadbeef" PROPERTY "gpio-reserved-ranges")
if(DEFINED reserved_ranges)
  # Node exists and has the "gpio-reserved-ranges" property.
endif()
```

要区分“节点不存在”和“属性不存在”，可组合使用 `dt_prop()` 与 `dt_node_exists()`：

```cmake
dt_node_exists(node_exists PATH "/soc/gpio@deadbeef")
dt_prop(reserved_ranges    PATH "/soc/gpio@deadbeef" PROPERTY "gpio-reserved-ranges")
if(DEFINED reserved_ranges)
  # Node "/soc/gpio@deadbeef" exists and has the "gpio-reserved-ranges" property
elseif(node_exists)
  # Node exists, but doesn't have the property, or the property has an unsupported type.
endif()
```

**`dt_comp_path`**

<a id="command:dt-comp-path"></a>

`dt_comp_path(<var> COMPATIBLE <compatible> [INDEX <idx>] [TARGET <target>])`

获取具有指定兼容字符串（Compatible）的节点路径列表，返回到 `<var>`。若不存在这样的兼容字符串，`<var>` 未定义。

有关 `<path>` 格式及返回参数的细节和注意事项，参见 `dt_prop()`。

- `<var>`：保存属性值的返回变量。
- `COMPATIBLE <compatible>`：要为其返回路径列表的兼容字符串，写法与 DTS 源文件相同。
- `INDEX <idx>`：取得数组属性中某个值时使用的可选索引。
- `TARGET <target>`：可选，指定从哪个目标取得设备树信息。

**`dt_num_regs`**

<a id="command:dt-num-regs"></a>

`dt_num_regs(<var> PATH <path> [TARGET <target>])`

获取节点 `reg` 属性中的寄存器块（Register Block）数量，可以为零。值返回到 `<var>`。

`<path>` 可以是节点的绝对路径 `/foo/bar`、节点别名 `my-alias`，或别名后接子节点路径 `my-alias/child-node`。

- `<var>`：保存属性值的返回变量。
- `PATH <path>`：节点路径。
- `TARGET <target>`：可选，指定从哪个目标取得设备树信息。

**`dt_reg_addr`**

<a id="command:dt-reg-addr"></a>

`dt_reg_addr(<var> PATH <path> [INDEX <idx>] [NAME <name>] [TARGET <target>])`

获取索引为 `<idx>` 或名称为 `<name>` 的寄存器块基地址（Base Address）。若两者均省略，返回索引 `0` 处的值；不得同时给出两者。值返回到 `<var>`。

`<path>` 可以是节点的绝对路径 `/foo/bar`、节点别名 `my-alias`，或别名后接子节点路径 `my-alias/child-node`。

结果可以是寄存器块的基地址；若节点不存在，或没有所请求索引或名称的寄存器块，`<var>` 未定义。

- `<var>`：保存地址值的返回变量。
- `PATH <path>`：节点路径。
- `INDEX <idx>`：寄存器块索引号。
- `NAME <name>`：寄存器块名称。
- `TARGET <target>`：可选，指定从哪个目标取得设备树信息。

**`dt_reg_size`**

<a id="command:dt-reg-size"></a>

`dt_reg_size(<var> PATH <path> [INDEX <idx>] [NAME <name>] [TARGET <target>])`

获取索引为 `<idx>` 或名称为 `<name>` 的寄存器块大小（Size）。若两者均省略，返回索引 `0` 处的值；不得同时给出两者。

原文称该值返回到 `<value>` 参数。`<path>` 可以是节点的绝对路径 `/foo/bar`、节点别名 `my-alias`，或别名后接子节点路径 `my-alias/child-node`。

- `<var>`：保存大小值的返回变量。
- `PATH <path>`：节点路径。
- `INDEX <idx>`：寄存器块索引号。
- `NAME <name>`：寄存器块名称。
- `TARGET <target>`：可选，指定从哪个目标取得设备树信息。

> 译注：概述中的 `<value>` 与本页签名和参数表不一致；返回变量实际由签名中的 `<var>` 指定。

**`dt_has_chosen`**

<a id="command:dt-has-chosen"></a>

`dt_has_chosen(<var> PROPERTY <prop> [TARGET <target>])`

检查设备树的 `/chosen` 节点是否具有给定属性 `<prop>`，且该属性包含某个节点的路径。检查结果以 `TRUE` 或 `FALSE` 保存到 `<var>`。

- `<var>`：返回变量。
- `PROPERTY <prop>`：chosen 属性。
- `TARGET <target>`：可选，指定从哪个目标取得设备树信息。

设备树片段示例：

```dts
chosen {
        foo = &bar;
};
```

使用示例：

```cmake
# Sets 'result' to TRUE
dt_has_chosen(result PROPERTY "foo")

# Sets 'result' to FALSE
dt_has_chosen(result PROPERTY "baz")
```

**`dt_chosen`**

<a id="command:dt-chosen"></a>

`dt_chosen(<var> PROPERTY <prop> [TARGET <target>])`

获取 `/chosen` 节点属性所对应的节点路径，返回到 `<var>`；chosen 节点不存在时，变量保持未定义。

- `<var>`：保存节点路径的返回变量。
- `PROPERTY <prop>`：chosen 属性。
- `TARGET <target>`：可选，指定从哪个目标取得设备树信息。

<a id="if-dt-node"></a>

### 8.4.2\_*_if_dt_node：按节点存在与否执行

本节类似于名为 `*_ifdef` 的扩展，但执行动作的条件是设备树包含某个节点。可以按需添加 `*_if_dt_node` 函数，也可在预计对用户应用有帮助时添加。

**`target_sources_if_dt_node`**

<a id="command:target-sources-if-dt-node"></a>

`target_sources_if_dt_node(<path> <target> <scope> <item>...)`

设备树节点存在时，向目标的 `SOURCES` 列表添加项目。

- `<path>`：要检查的设备树节点路径。
- `<target>`：要向其添加源文件的构建系统目标。
- `<scope>`：添加项目所使用的作用域。
- `<item>`：要加入目标的一个或多个项目。

使用示例：

```cmake
# If the devicetree alias "led0" refers to a node, this
# adds "blink_led.c" to the sources list for the "app" target.
target_sources_if_dt_node("led0" app PRIVATE blink_led.c)

# If the devicetree path "/soc/serial@4000" is a node, this
# adds "uart.c" to the sources list for the "lib" target,
target_sources_if_dt_node("/soc/serial@4000" lib PRIVATE uart.c)
```

<a id="zephyr-dt"></a>

### 8.4.3\_zephyr_dt_*：处理设备树文件

下列方法是 CMake 中处理设备树相关文件的共用代码。访问设备树内容的函数属于前面的 `dt_*` 部分；本节仅处理配置阶段（Configuration Time）的设备树文件。

**`zephyr_dt_preprocess`**

<a id="command:zephyr-dt-preprocess-cpp"></a>

`zephyr_dt_preprocess(CPP <path> [<argument...>] SOURCE_FILES <file...> OUT_FILE <file> [DEPS_FILE <file> [EXTRA_CPPFLAGS <flag...>] [INCLUDE_DIRECTORIES <dir...>] [WORKING_DIRECTORY <dir>])`

预处理（Preprocess）一个或多个设备树源文件，并定义预处理器符号 `__DTS__`。若预处理器命令失败，产生致命错误。

必需参数：

- `CPP <path> [<argument...>]`：C 预处理器的路径，后接额外参数。
- `SOURCE_FILES <file...>`：要预处理的源文件；效果相当于按顺序拼接它们，作为预处理器输入。
- `OUT_FILE <file>`：保存预处理器输出的位置。

可选参数：

- `DEPS_FILE <file>`：设置时，在此位置生成依赖文件（Dependency File）。
- `EXTRA_CPPFLAGS <flag...>`：传给预处理器的额外选项。
- `INCLUDE_DIRECTORIES <dir...>`：额外的 `#include` 文件目录。
- `WORKING_DIRECTORY <dir>`：运行预处理器的目录。

**`zephyr_dt_import`**

<a id="command:zephyr-dt-import-edt-pickle-file"></a>

`zephyr_dt_import(EDT_PICKLE_FILE <file> TARGET <target>)`

解析设备树信息并提供给 CMake，以便通过设备树读取部分的 `dt_*` CMake 扩展访问。

这需要运行一个 Python 脚本，将 edtlib 的输出转换为 CMake 源文件。脚本失败时，产生致命错误。

- `EDT_PICKLE_FILE <file>`：以 pickle 格式保存的输入 `edtlib.EDT` 对象。
- `TARGET <target>`：要填入设备树属性的目标。

<a id="zephyr-linker-functions"></a>

## 8.5\_Zephyr链接器函数（Linker Functions）

<a id="zephyr-linker"></a>

### 8.5.1\_zephyr_linker*：定义链接布局

下列方法通过 CMake 函数定义链接器结构，使 Zephyr 开发者能够定义链接节（Linker Section）及其内容，再按所用工具链生成适当的链接脚本。例如，GNU ld 使用 ld 链接脚本，ARM 链接器使用 ARM 散布加载文件（Scatter File）。

使用示例：

```cmake
zephyr_linker_section(
  NAME my_data
  VMA  RAM
  LMA  FLASH
)

# and to configure special input sections for the section
zephyr_linker_section_configure(
  SECTION my_data
  INPUT   "my_custom_data"
  KEEP
)
```

**`zephyr_linker`**

<a id="command:zephyr-linker"></a>

`zephyr_linker([FORMAT <format>] [ENTRY <entry_symbol>])`

配置 Zephyr 链接器（Linker）的通用设置，指定待生成链接脚本（Linker Script）的常规设置。

- `FORMAT <format>`：链接后可执行文件的输出格式。
- `ENTRY <entry_symbol>`：代码入口符号。

**`zephyr_linker_memory`**

<a id="command:zephyr-linker-memory-name"></a>

`zephyr_linker_memory(NAME <name> START <address> SIZE <size> [FLAGS <flags>])`

为当前平台指定链接器内存区域（Memory Region）。

**注意：**通常应使用从设备树或 Kconfig 取得的值调用此函数。

- `NAME <name>`：内存区域名称，例如 `FLASH`。
- `START <address>`：内存区域起始地址，可以是十进制或十六进制。
- `SIZE <size>`：区域大小，可以是十进制、十六进制，或带 `k`／`m` 后缀的十进制。`1048576`、`0x10000`、`1024k`、`1024K`、`1m`、`1M` 都是有效值。
- `FLAGS <flags>`：描述区域属性的标志。

各标志的含义：`r` 为只读区域，`w` 为可读写区域，`x` 为可执行区域，`a` 为可分配区域，`i` 为已初始化区域，`l` 与 `i` 相同；`!` 反转其后属性的含义。可组合使用，例如 `rx`、`rx!w`。

**`zephyr_linker_memory_ifdef`**

<a id="command:zephyr-linker-memory-ifdef"></a>

`zephyr_linker_memory_ifdef(<setting> NAME <name> START <address> SIZE <size> [FLAGS <flags>])`

当 `<setting>` 启用时创建内存区域。调用 `zephyr_linker_memory()` 之前，检查 `<setting>` 是否为真。其他支持的参数见 `zephyr_linker_memory()`。

**`zephyr_linker_dts_section`**

<a id="command:zephyr-linker-dts-section-path"></a>

`zephyr_linker_dts_section(PATH <path>)`

根据设备树配置，通过节点路径为当前平台指定链接器输出节（Output Section）。仅在设备树节点存在且状态为 `okay` 时定义该节。

`PATH <path>` 为设备树节点路径。

**`zephyr_linker_dts_memory`**

<a id="command:zephyr-linker-dts-memory-path"></a>

`zephyr_linker_dts_memory(PATH <path>)`

<a id="command:zephyr-linker-dts-memory-nodelabel"></a>

`zephyr_linker_dts_memory(NODELABEL <nodelabel>)`

<a id="command:zephyr-linker-dts-memory-chosen"></a>

`zephyr_linker_dts_memory(CHOSEN <prop>)`

根据设备树配置，为当前平台指定链接器内存区域。仅在设备树节点或与节点标签匹配的节点存在、且状态为 `okay` 时，才定义内存区域。

`PATH`、`NODELABEL`、`CHOSEN` 三个参数只能给出一个。

- `PATH <path>`：设备树节点标识。
- `NODELABEL <label>`：节点标签。
- `CHOSEN <prop>`：chosen 属性；若存在，添加 `/chosen` 属性所描述的内存节。

**`zephyr_linker_group`**

<a id="command:zephyr-linker-group-name"></a>

`zephyr_linker_group(NAME <name> [VMA <region|group>] [LMA <region|group>] [GROUP <group>] [SYMBOL <SECTION>])`

在内存区域或另一个组中指定链接器组（Linker Group）。组确保内部所有节一起位于指定组中。

这也允许将节放入给定组，而节本身无须确切知道最终落入哪个内存区域；该区域由组的配置决定。

每组定义以下链接器符号：`__name_start` 为组起始地址，`__name_end` 为结束地址，`__name_size` 为大小。定义链接器符号时，`<name>` 转为小写。

- `NAME <name>`：组名。
- `VMA <region|group>`：该组使用的虚拟内存地址（Virtual Memory Address，VMA）区域或组；若指定组，使用该组的 VMA 区域。
- `LMA <region|group>`：该组使用的加载内存地址（Load Memory Address，LMA）区域或组。
- `GROUP <group>`：把新组放入已有 `<group>` 内。
- `SYMBOL <SECTION>`：指定区域的起始符号应等于组中第一个节的起始地址。

**注意：**`VMA` 和 `LMA` 与 `GROUP` 互斥。

以下示例中，`groupB` 从 `groupA` 继承 LMA，因此会在同一内存区域创建两个组：

```cmake
zephyr_linker_memory(NAME memA START ... SIZE ... FLAGS ...)
zephyr_linker_group(NAME groupA LMA memA)
zephyr_linker_group(NAME groupB LMA groupA)
```

```text
+-----------------+
| memory region A |
|                 |
| +-------------+ |
| | groupA      | |
| +-------------+ |
|                 |
| +-------------+ |
| | groupB      | |
| +-------------+ |
|                 |
| +-------------+ |
```

而下面的写法会在 `groupA` 内部创建 `groupB`：

```cmake
zephyr_linker_memory(NAME memA START ... SIZE ... FLAGS ...)
zephyr_linker_group(NAME groupA LMA memA)
zephyr_linker_group(NAME groupB GROUP groupA)
```

```text
+---------------------+
| memory region A     |
|                     |
| +-----------------+ |
| | groupA          | |
| |                 | |
| | +-------------+ | |
| | | groupB      | | |
| | +-------------+ | |
| |                 | |
| +-----------------+ |
|                     |
+---------------------+
```

**`zephyr_linker_section`**

<a id="command:zephyr-linker-section-name"></a>

`zephyr_linker_section(NAME <name> [GROUP <group>] [VMA <region|group>] [LMA <region|group>] [ADDRESS <address>] [ALIGN <alignment>] [SUBALIGN <alignment>] [FLAGS <flags>] [MIN_SIZE <size>] [MAX_SIZE <size>] [HIDDEN] [NOINPUT] [NOINIT] [PASS [NOT] <name>...])`

为链接器指定输出节（Output Section）。

`zephyr_linker_section(NAME <name>)` 配置名为 `<name>` 的输出节。除非指定 `NOINPUT`，默认包含同名输入节（Input Section）；例如，名为 `foo` 的节默认包含匹配 `foo` 和 `foo.*` 的输入节。

每个输出节定义以下链接器符号：

- `__name_start`：节起始地址。
- `__name_end`：节结束地址。
- `__name_size`：节大小。
- `__name_load_start`：节加载地址；若 VMA 等于 LMA，与 `__name_start` 相同。

可通过 `LMA`、`VMA` 和地址参数控制输出节位置。

- `NAME <name>`：输出节名称。
- `VMA <region|group>`：代码或数据运行时所在的 VMA 内存区域或组。指定组时，只使用该组的 VMA 内存区域，并不把节放到组内；另见 `GROUP`。
- `KVMA <region|group>`：内核运行时的 VMA 区域或组。内存管理单元（Memory Management Unit，MMU）启用且内核虚拟内存（Virtual Memory，VM）的基址及偏移不同于 SRAM 时，使用 `KVMA` 定义的区域作为 VMA。指定组时，同样只是使用该组的 VMA 区域，不放入组内。
- `LMA <region|group>`：代码或数据加载时所在的区域或组。VMA 与 LMA 不同时，启动时将内容从 LMA 加载到 VMA；典型情况是映像中位于 ROM、启动时复制到 RAM 的全局或静态变量。指定组时，仅使用该组的 LMA 内存区域，并不放入组内。
- `GROUP <group>`：将此节放入 `<group>`。
- `ADDRESS <address>`：此节使用的指定地址。
- `ALIGN_WITH_INPUT`：保持此节 VMA 与 LMA 之间的对齐差值。
- `ALIGN <alignment>`：按指定对齐值对齐执行地址。
- `SUBALIGN <alignment>`：按指定对齐值对齐输入节。
- `ENDALIGN <alignment>`：对齐节末尾，使下一输出节起点对齐；只对散布加载脚本（Scatter Script）生效。

**关于对齐属性的注意事项：**并非所有链接器都以相同方式处理对齐。例如，散布加载文件在给出 `ALIGN` 时，会同时对齐加载地址和执行地址，即 LMA 和 VMA。

- `MIN_SIZE <size>`：填充节，使其至少有 `<size>` 字节。
- `MAX_SIZE <size>`：检查节不超过 `<size>` 字节。
- `NOINPUT`：不定义默认输入节。要为 `<name>` 设置输入节，必须使用对应的 `zephyr_linker_section_configure()`。
- `PASS [NOT] <name>...`：指定节生效的链接轮次（Linker Pass）。默认存在于全部轮次。`PASS <p1> <p2>...` 表示只在给定轮次存在，空列表表示不在任何轮次存在；`PASS NOT <p1> <p2>...` 表示在排除给定轮次后的所有轮次存在，空列表表示全部轮次。
- `TYPE <type>`：标记节以进行特殊处理。`NOLOAD`、`BSS` 确保节为 `NOLOAD`；`LINKER_SCRIPT_FOOTER` 表示唯一一个应最后生成的节。

**注意：**`VMA` 和 `LMA` 与 `GROUP` 互斥。

> 译注：原页签名和参数正文覆盖范围并不完全相同；这里保留两者，未把签名中缺少逐项解释的 `FLAGS`、`HIDDEN`、`NOINIT` 自行补写为官方定义。

**`zephyr_linker_section_ifdef`**

<a id="command:zephyr-linker-section-ifdef"></a>

`zephyr_linker_section_ifdef(<setting> NAME <name> [GROUP <group>] [VMA <region|group>] [LMA <region|group>] [ADDRESS <address>] [ALIGN <alignment>] [SUBALIGN <alignment>] [FLAGS <flags>] [MIN_SIZE <size>] [MAX_SIZE <size>] [HIDDEN] [NOINPUT] [NOINIT] [PASS [NOT] <name>...])`

当 `<setting>` 启用时创建输出节。调用 `zephyr_linker_section()` 之前，检查 `<setting>` 是否为真。其他支持的参数见 `zephyr_linker_section()`。

**`zephyr_iterable_section`**

<a id="command:zephyr-iterable-section-name"></a>

`zephyr_iterable_section(NAME <name> [GROUP <group>] [VMA <region|group>] [LMA <region|group>] [ALIGN_WITH_INPUT] [SUBALIGN <alignment>])`

定义输出节，建立由等大小数据结构组成的可迭代区域（Iterable Area），供 `STRUCT_SECTION_ITERABLE` 使用。输入节默认按名称的字典顺序（Lexicographical Order）排序。

每个输入节列表定义 `_<name>_list_start` 和 `_<name>_list_end`，分别表示可迭代列表的开始和结束。

输出节名为 `<name>_area`，定义以下链接器符号：

| 符号 | 含义 |
| --- | --- |
| `__name_area_start` | 节起始地址 |
| `__name_area_end` | 节结束地址 |
| `__name_area_size` | 节大小 |
| `__name_area_load_start` | 节加载地址；VMA 等于 LMA 时，与 `__name_area_start` 相同 |

支持的选项如下：

- `NAME <name>`：结构体类型名称，相应输出节命名为 `<name>_area`。
- `VMA <region|group>`：代码或数据运行时所在的 VMA 内存区域。
- `LMA <region|group>`：代码或数据加载时所在区域。VMA 与 LMA 不同时，启动时从 LMA 加载到 VMA；典型情况是存放在 ROM、启动时复制到 RAM 的全局或静态变量。
- `GROUP <group>`：将此节放入 `<group>`。
- `ADDRESS <address>`：此节使用的指定地址。
- `ALIGN_WITH_INPUT`：保持 VMA 与 LMA 之间的对齐差值。
- `NUMERIC`：使用数值排序（Numeric Sorting）。
- `SUBALIGN <alignment>`：按 `<alignment>` 强制输入对齐。

**注意：**并非所有链接器对齐行为都相同。例如，在散布加载文件中给出 `ALIGN` 时，会同时对齐加载和执行地址，即 LMA 和 VMA。

**`zephyr_linker_section_obj_level`**

<a id="command:zephyr-linker-section-obj-level-section"></a>

`zephyr_linker_section_obj_level(SECTION <section> LEVEL <level>)`

为指定对象和级别生成符号，标记对象数组的起点，再链接全部这些对象，并按优先级排序。即使没有直接引用，也确保对象不会被丢弃。这对 `struct devices` 等内容很有用。

例如，`zephyr_linker_section_obj_level(SECTION init LEVEL PRE_KERNEL_1)` 会创建匹配 `.z_init_PRE_KERNEL_P_1_SUB_?_`、`.z_init_PRE_KERNEL_P_1_SUB_??_` 和 `.z_init_PRE_KERNEL_P_1_SUB_???_` 的输入节。

- `SECTION <section>`：放置对象的节。
- `LEVEL <level>`：优先级级别；匹配该级别的全部输入节都将排序。

**`zephyr_linker_section_configure`**

<a id="command:zephyr-linker-section-configure-section"></a>

`zephyr_linker_section_configure(SECTION <section> [ALIGN <alignment>] [PASS [NOT] <name>] [PRIO <no>] [SORT <sort>] [MIN_SIZE <size>] [MAX_SIZE <size>] [ANY] [FIRST] [KEEP] [INPUT <input>] [SYMBOLS [<start> [<end>]]])`

为输出节配置额外输入节。输出节除默认输入节外，还可包含更多输入节。例如，要把输入节 `foo` 加入输出节 `bar`，并带上 `KEEP` 属性，可调用 `zephyr_linker_section_configure(SECTION bar INPUT foo KEEP)`。

- `SECTION <section>`：要配置的输出节。
- `ALIGN <alignment>`：按 `<alignment>` 对齐输入节在加载区域中的位置。
- `FIRST`：把列表中的第一个输入节标记为输出中的首节。
- `SORT <NAME>`：按 `<type>` 对输入节排序，目前只支持 `NAME`。
- `MIN_SIZE <size>`：填充节，使其至少有 `<size>` 字节。
- `MAX_SIZE <size>`：检查节不超过 `<size>` 字节。
- `KEEP`：链接期间不移除此输入节。
- `PRIO`：输入节优先级。默认情况下，并非所有链接器都保证输入节顺序；指定优先级后，Zephyr 的 CMake 链接器配置会以可保证顺序的方式创建节。未指定优先级的节，按 CMake 处理顺序从 `100` 开始分配内部优先级，依次为 `100`、`101` 等。希望某个节排在这些节之前，可用 `PRIO 50`、`PRIO 20` 等；希望位于末尾，建议用 `PRIO 200` 或更高值。
- `PASS [NOT] <pass>...`：控制这部分内容出现在哪些链接轮次；详见 `zephyr_linker_section()` 的 `PASS`。
- `FLAGS <flags>`：特殊节标志，例如 `+RO`、`+XO`、`+ZI`。`FLAGS` 和 `ANY` 只对散布加载文件生效。
- `ANY`：散布加载文件的 `ANY` 节标志，同样只对这种文件生效。
- `INPUT <input>`：输入节名或节名列表。`<input>` 可以只是 `.data*` 这样的节名，也可以是 `<file-pattern>(<section-patterns>... )`；其中 `<file-pattern>` 为 `[library.a:]file`，例如 `foo.a:bar.o(.data*)`。
- `SYMBOLS <start> <end>`：为输入节生成开始和结束符号。

**`zephyr_linker_symbol`**

<a id="command:zephyr-linker-symbol-symbol"></a>

`zephyr_linker_symbol(SYMBOL <name> EXPR <expr>)`

向生成的链接脚本添加用户定义的额外符号。

- `SYMBOL <name>`：要提供的符号名称。
- `EXPR <expr>`：定义符号的表达式。受链接器限制，表达式应只包含 `+, -, *` 等简单运算。表达式直接传入链接器，其中所有 `@<symbol>@` 替换为所引用的符号。

例如，要创建新符号 `bar`，使其指向节 `foo` 的起始 VMA 地址加 `1024`，可以写：

```cmake
zephyr_linker_symbol(SYMBOL bar EXPR "(@foo@ + 1024)")
```

**`zephyr_linker_include_generated`**

<a id="command:zephyr-linker-include-generated"></a>

`zephyr_linker_include_generated((CMAKE | KCONFIG | HEADER) <name> [PASS [NOT] <pass>...])`

添加构建时生成的文件，在运行链接脚本生成器时加载。

- `CMAKE <name>`：包含给定 CMake 文件。
- `KCONFIG <name>`：对给定 Kconfig 文件调用 `import_kconfig()`，使全部 `CONFIG_FOO` 设置可通过 `@variable@` 访问。
- `HEADER <name>`：查找 `name` 中的所有 `#define FOO value`。只用普通正则表达式（Regular Expression），不进行完整预处理。
- `PASS [NOT] <pass>...`：决定哪些链接轮次包含该文件；见 `zephyr_linker_section()` 的 `PASS`。

**`zephyr_linker_include_var`**

<a id="command:zephyr-linker-include-var-var"></a>

`zephyr_linker_include_var(VAR <name> [VALUE <value>] [PASS [NOT] <pass>...])`

保存 `<name>` 的值，供生成器在构建时运行时使用。若未设置 `VALUE`，使用变量当前值。

- `VAR <name>`：要设置的变量。
- `VALUE <value>`：该值。
- `PASS [NOT] <pass>...`：决定哪些链接轮次包含该变量；详见 `zephyr_linker_section()` 的 `PASS`。

**`zephyr_linker_generate_linker_settings_file`**

<a id="command:zephyr-linker-generate-linker-settings-file"></a>

`zephyr_linker_generate_linker_settings_file(<file_name>)`

为链接文件生成器脚本生成一个设置文件。`<file_name>` 是要创建的文件。

<a id="function-helper-macros"></a>

## 8.6\_函数辅助宏（Function Helper Macros）

本节提供一组 CMake 宏，用于简化定义函数时的参数处理。

**`zephyr_check_arguments_required`**

<a id="command:zephyr-check-arguments-required"></a>

`zephyr_check_arguments_required(<function_name> <prefix> <arg1> [<arg2> ...])`

检查调用者是否至少提供了一个必需参数的辅助宏（Helper Macro）。如果必需参数一个也未传入，则产生 `FATAL_ERROR`。

- `<function_name>`：所检查的函数名称，用于生成错误消息。
- `<prefix>`：`cmake_parse_arguments` 所用前缀，通常为 `arg` 或大写函数名。
- `<arg>`：要检查的一个或多个参数。

**`zephyr_check_arguments_required_allow_empty`**

<a id="command:zephyr-check-arguments-required-allow-empty"></a>

`zephyr_check_arguments_required_allow_empty(<function_name> <prefix> <arg1> [<arg2> ...])`

检查调用者是否至少提供了一个必需参数的辅助宏，允许参数值为空。如果必需参数一个也未传入，则产生 `FATAL_ERROR`。

- `<function_name>`：所检查的函数名称，用于生成错误消息。
- `<prefix>`：`cmake_parse_arguments` 所用前缀，通常为 `arg` 或大写函数名。
- `<arg>`：要检查的一个或多个参数。

**`zephyr_check_flags_required`**

<a id="command:zephyr-check-flags-required"></a>

`zephyr_check_flags_required(<function_name> <prefix> <flag1> [<flag2> ...])`

检查调用者是否至少提供了一个必需标志（Flag）的辅助宏。如果必需标志一个也未传入，则产生 `FATAL_ERROR`。

- `<function_name>`：所检查的函数名称，用于生成错误消息。
- `<prefix>`：`cmake_parse_arguments` 所用前缀，通常为 `arg` 或大写函数名。
- `<flag>`：要检查的一个或多个标志。

**`zephyr_check_arguments_required_all`**

<a id="command:zephyr-check-arguments-required-all"></a>

`zephyr_check_arguments_required_all(<function_name> <prefix> <arg1> [<arg2> ...])`

检查调用者是否提供了全部必需参数的辅助宏。缺少任何一个必需参数，都会产生 `FATAL_ERROR`。

- `<function_name>`：所检查的函数名称，用于生成错误消息。
- `<prefix>`：`cmake_parse_arguments` 所用前缀，通常为 `arg` 或大写函数名。
- `<arg>`：要检查的一个或多个参数。

**`zephyr_check_arguments_exclusive`**

<a id="command:zephyr-check-arguments-exclusive"></a>

`zephyr_check_arguments_exclusive(<function_name> <prefix> <arg1> <arg2> [<arg3> ...])`

检查互斥参数（Mutually Exclusive Argument）是否未被同时提供的辅助宏。如果任何互斥参数同时出现，则产生 `FATAL_ERROR`。

- `<function_name>`：所检查的函数名称，用于生成错误消息。
- `<prefix>`：`cmake_parse_arguments` 所用前缀，通常为 `arg` 或大写函数名。
- `<arg>`：要检查的一个或多个参数。

**`zephyr_check_flags_exclusive`**

<a id="command:zephyr-check-flags-exclusive"></a>

`zephyr_check_flags_exclusive(<function_name> <prefix> <flag1> <flag2> [<flag3> ...])`

检查互斥标志（Mutually Exclusive Flag）是否未被同时提供的辅助宏。如果任何互斥标志同时出现，则产生 `FATAL_ERROR`。

- `<function_name>`：所检查的函数名称，用于生成错误消息。
- `<prefix>`：`cmake_parse_arguments` 所用前缀，通常为 `arg` 或大写函数名。
- `<flag>`：要检查的一个或多个标志。

**`zephyr_check_no_arguments`**

<a id="command:zephyr-check-no-arguments"></a>

`zephyr_check_no_arguments(<function_name> <arg1> [<arg2> ...])`

检查是否未提供任何意外参数的辅助宏。只要出现意外参数，就产生 `FATAL_ERROR`。

- `<function_name>`：所检查的函数名称，用于生成错误消息。
- `<arg>`：要检查的一个或多个参数。

<a id="linkable-loadable-extensions-llext"></a>

## 8.7\_可链接可加载扩展（Linkable Loadable Extensions，LLEXT）

这些函数简化可链接可加载扩展（Linkable Loadable Extensions，LLEXT）的创建和管理。

<a id="configuration-functions"></a>

### 8.7.1\_配置函数（Configuration Functions）

下列函数采用与 CMake `target_*` 函数相同的 API，简化 LLEXT 编译和链接阶段属性的访问。

**`llext_compile_definitions`**

<a id="command:llext-compile-definitions-target-name"></a>

`llext_compile_definitions(target_name <defs>...)`

向可链接可加载扩展（Linkable Loadable Extension，LLEXT）目标添加编译宏定义。

- `target_name`：LLEXT 目标名称。
- `<defs>`：传给 `target_compile_definitions` 的参数。

**`llext_compile_features`**

<a id="command:llext-compile-features-target-name"></a>

`llext_compile_features(target_name <features>...)`

向 LLEXT 目标添加编译特性（Compile Feature）。

- `target_name`：LLEXT 目标名称。
- `<features>`：传给 `target_compile_features` 的参数。

**`llext_compile_options`**

<a id="command:llext-compile-options-target-name"></a>

`llext_compile_options(target_name <options>...)`

向 LLEXT 目标添加编译选项（Compile Option）。

- `target_name`：LLEXT 目标名称。
- `<options>`：传给 `target_compile_options` 的参数。

**`llext_include_directories`**

<a id="command:llext-include-directories-target-name"></a>

`llext_include_directories(target_name <dirs>...)`

向 LLEXT 目标添加包含目录（Include Directory）。

- `target_name`：LLEXT 目标名称。
- `<dirs>`：传给 `target_include_directories` 的参数。

**`llext_link_options`**

<a id="command:llext-link-options-target-name"></a>

`llext_link_options(target_name <options>...)`

向 LLEXT 目标添加链接选项（Link Option）。

- `target_name`：LLEXT 目标名称。
- `<options>`：传给 `target_link_options` 的参数。

<a id="build-control-functions"></a>

### 8.7.2\_构建控制函数（Build Control Functions）

下列函数向构建系统添加目标和子命令，用于编译和链接 LLEXT。

**`add_llext_target`**

<a id="command:add-llext-target-target-name-output"></a>

`add_llext_target(target_name OUTPUT <output_file> SOURCES <source_files>)`

添加自定义目标，将一组源文件编译为 `.llext` 文件。必须通过 `OUTPUT` 和 `SOURCES` 指定输出和源文件。

选择 `CONFIG_LLEXT_TYPE_ELF_OBJECT` 时，只支持一个源文件，因为此时没有链接步骤。

LLEXT 代码使用的 C 编译器选项大体与 Zephyr 构建相同，但有若干重要修改。移除和追加的选项列表，分别由全局变量 `LLEXT_REMOVE_FLAGS` 和 `LLEXT_APPEND_FLAGS` 控制。

`target_name` 定义以下自定义属性，可通过 `get_target_property` 取得：

- `lib_target`：执行源文件编译及／或链接步骤的目标名称。
- `lib_output`：编译及／或链接得到的二进制文件。
- `pkg_input`：打包（Packaging）步骤的输入文件。
- `pkg_output`：最终 `.llext` 文件。

使用示例：

```cmake
add_llext_target(hello_world
  OUTPUT  ${PROJECT_BINARY_DIR}/hello_world.llext
  SOURCES ${PROJECT_SOURCE_DIR}/src/llext/hello_world.c
)
```

这会将源文件 `src/llext/hello_world.c` 编译为名为 `$PROJECT_BINARY_DIR/hello_world.llext` 的文件。

> 译注：上句保留原文的变量展示形式；若在 CMake 表达式中引用该变量，应写 `${PROJECT_BINARY_DIR}`。原页源文件名末尾还有一个多余反引号，译文已去除。

**`add_llext_command`**

<a id="command:add-llext-command-target"></a>

`add_llext_command(TARGET <target_name> PRE_BUILD <command> [...])`

向 LLEXT 目标添加构建期间执行的自定义命令。命令在指定构建步骤执行，可以引用 `<target>` 的属性，取得与该次构建有关的细节。

不同构建步骤的含义如下：

- `PRE_BUILD`：架构使用动态库（Dynamic Library）时，在 LLEXT 代码链接前执行。此步骤可访问 `lib_target` 及其自身属性。
- `POST_BUILD`：在 LLEXT 代码构建完成后、打包到 `.llext` 文件之前执行。预期读取 `lib_output` 内容并创建 `pkg_input` 文件。
- `POST_PKG`：在 `.llext` 文件创建后执行，可以操作最终 LLEXT 文件 `pkg_output`。

`COMMAND` 之后的所有内容，原样传给 `add_custom_command`，包括多个命令及其他选项。

## 8.8\_原文相关参考

- [CMake library](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html)
- [target_sources](https://cmake.org/cmake/help/latest/command/target_sources.html#command:target_sources)
- [target_include_directories](https://cmake.org/cmake/help/latest/command/target_include_directories.html#command:target_include_directories)
- [target_compile_definitions](https://cmake.org/cmake/help/latest/command/target_compile_definitions.html#command:target_compile_definitions)
- [target_compile_options](https://cmake.org/cmake/help/latest/command/target_compile_options.html#command:target_compile_options)
- [target_link_libraries](https://cmake.org/cmake/help/latest/command/target_link_libraries.html#command:target_link_libraries)
- [LIBC_LINK_LIBRARIES](P019_LIBC_LINK_LIBRARIES.md#prop_tgt:LIBC_LINK_LIBRARIES)
- [ZEPHYR_CURRENT_LIBRARY](P059_ZEPHYR_CURRENT_LIBRARY.md#variable:ZEPHYR_CURRENT_LIBRARY)
- [manual:cmake-commands(7)](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html#manual:cmake-commands%287%29)
- [add_dependencies()](https://cmake.org/cmake/help/latest/command/add_dependencies.html#command:add_dependencies)
- [K_APPMEM_PARTITION_DEFINE](../memory_domain_reference/P006_应用内存分区接口.md#gaba1614a7fa1a2ce2fc7cfd6ecfc02796)
- [tests/application_development/gen_inc_file](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/application_development/gen_inc_file)
- [ACTIVE_BOARD_REVISION](P020_ACTIVE_BOARD_REVISION.md#variable:ACTIVE_BOARD_REVISION)
- [Kconfig](https://docs.zephyrproject.org/latest/build/kconfig/index.html#kconfig)
- [file(COPY_FILE...)](https://cmake.org/cmake/help/latest/command/file.html#copy-file)
- [string](https://cmake.org/cmake/help/latest/command/string.html#command:string)
- [list(TRANSFORM ...)](https://cmake.org/cmake/help/latest/command/list.html#transform)
- [configure_file](https://cmake.org/cmake/help/latest/command/configure_file.html#command:configure_file)
- [ZEPHYR_TOOLCHAIN_VARIANT](https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-ZEPHYR_TOOLCHAIN_VARIANT)
- [scripts/schemas/build-schema.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/schemas/build-schema.yaml)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [cmake_parse_arguments](https://cmake.org/cmake/help/latest/command/cmake_parse_arguments.html#command:cmake_parse_arguments)
- [Linkable Loadable Extensions (LLEXT)](https://docs.zephyrproject.org/latest/services/llext/index.html#llext)
- [target_compile_features](https://cmake.org/cmake/help/latest/command/target_compile_features.html#command:target_compile_features)
- [target_link_options](https://cmake.org/cmake/help/latest/command/target_link_options.html#command:target_link_options)
- [CONFIG_LLEXT_TYPE_ELF_OBJECT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLEXT_TYPE_ELF_OBJECT)
- [LLEXT_REMOVE_FLAGS](P042_LLEXT_REMOVE_FLAGS.md#variable:LLEXT_REMOVE_FLAGS)
- [LLEXT_APPEND_FLAGS](P041_LLEXT_APPEND_FLAGS.md#variable:LLEXT_APPEND_FLAGS)
- [get_target_property](https://cmake.org/cmake/help/latest/command/get_target_property.html#command:get_target_property)
- [add_custom_command](https://cmake.org/cmake/help/latest/command/add_custom_command.html#command:add_custom_command)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：basic_settings](P007_basic_settings.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：kconfig](P009_kconfig.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P007_basic_settings.md) · [返回大纲](大纲.md) · [下一章](P009_kconfig.md)

</details>

<!-- reading-navigation:end -->
