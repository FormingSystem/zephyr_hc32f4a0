# 构建后的 SDK 选择与证据核验

这是一页可选对照实验，入口是已经完成 P002—P005 的环境与依赖准备，并在 [P008](../P008_选择应用与硬件目标并构建.md)构建过 hello_world 的 Windows UCRT64 读者。安装 SDK 本身见 [P004](../P004_SDK准备与编译器选型.md)，首次学习不用来回跳转执行。这里沿用同一个应用和板目标，只改变工具链发现方式，并用独立构建目录记录结果。

<a id="sdk-configure"></a>

## 1. 显式指定 SDK 根

示例使用当前官方源码已有的 `samples/hello_world` 与 `mps2/an386`：MPS2 的 AN386 目标，Cortex-M4，适合后续 QEMU 演示。它不是 HC32 实板；HC32 的适配在 P014 完成。执行前确认源码中有 `samples/hello_world/CMakeLists.txt`、`boards/arm/mps2`，P003 的 `.venv` 及依赖可用，P005 中清单指定的 cmsis 与 cmsis_6 均已取得，MPS2 的外设底层由树内 CMSDK 驱动提供，并使用尚未配置的新 `-B` 目录。

```bash
# Windows UCRT64；P003 环境与 P005 两个 CMSIS 模块已准备；使用新构建目录。
(
set -e
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
test -f ../modules/hal/cmsis/zephyr/module.yml
test -f ../modules/hal/cmsis_6/CMSIS/Core/Include/core_cm4.h
MSYS2_ARG_CONV_EXCL='*' /ucrt64/bin/cmake \
  -S "$(cygpath -am samples/hello_world)" -B "$(cygpath -am build/learning-tools/p003/sdk-explicit)" \
  -G Ninja -DBOARD=mps2/an386 \
  "-DZephyr_DIR=$(cygpath -am share/zephyr-package/cmake)" \
  "-DPYTHON_EXECUTABLE=$(cygpath -am .venv/Scripts/python.exe)" "-DPython3_EXECUTABLE=$(cygpath -am .venv/Scripts/python.exe)" \
  "-DCMAKE_MAKE_PROGRAM=$(cygpath -am /ucrt64/bin/ninja.exe)" \
  "-DZEPHYR_MODULES=$(cygpath -am ../modules/hal/cmsis);$(cygpath -am ../modules/hal/cmsis_6)" \
  "-DZEPHYR_SDK_INSTALL_DIR=$(cygpath -am ../zephyr-sdk-1.0.1)" \
  -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
)
```

**参数定位：上方代码块。** 行号从块内首行起算，注释和空行计入；自动折行不计。

<!-- parameter-lines:start -->
| 块内行号 | 原样参数片段 | 读取者与作用 |
| --- | --- | --- |
| 8 | `MSYS2_ARG_CONV_EXCL` | 本次关闭自动参数转换 |
| 9 | `-S` | 应用入口与独立构建目录 |
| 10 | `-G Ninja` | 选择 Ninja 与板目标 |
| 11 | `-DZephyr_DIR=` | 当前 Zephyr 源码包入口 |
| 12 | `-DPYTHON_EXECUTABLE=` | 两个 Python 接口指向同一 Windows venv |
| 13 | `-DCMAKE_MAKE_PROGRAM=` | 固定 UCRT64 Ninja |
| 14 | `-DZEPHYR_MODULES=` | 本例完整 CMSIS 模块列表，保持为一个参数 |
| 15 | `-DZEPHYR_SDK_INSTALL_DIR=` | SDK 安装根 |
| 16 | `-DCMAKE_EXPORT_COMPILE_COMMANDS=` | 生成编译命令数据库 |
<!-- parameter-lines:end -->

这两条 SDK 对照路线显式传入本例所需的 cmsis 与 cmsis_6，因此 Git 下载和 ZIP 下载都能使用；P005 若采用其他模块目录，应同时调整检查与传参路径。`ZEPHYR_MODULES` 是完整列表，这里的两项仅服务 hello_world + mps2/an386，不能直接作为其他产品的通用列表。普通工程的 west 自动发现路线仍按 P008 选择。

括号创建子 shell，`set -e` 让前置检查或配置失败后停止本块，同时不退出读者的交互终端。CMake 与 Ninja 固定来自 `/ucrt64/bin`，Python 固定为项目 `.venv/Scripts/python.exe`。所有跨进程路径先由 `cygpath -am` 转换，再仅对 CMake 这一调用禁用自动参数转换，避免分号模块列表被二次解释。

这条命令在配置/生成阶段接入 SDK，不调用 `cmake --build`。`-S` 选应用、`-B` 指定本次生成目录；`Zephyr_DIR` 定位当前源码，`Python3_EXECUTABLE` 选择已激活环境中的解释器；本实验指定 SDK 的输入是 `-DZEPHYR_SDK_INSTALL_DIR=...`。`CMAKE_EXPORT_COMPILE_COMMANDS=ON` 用于后面的观察，不是 SDK 发现条件。`cygpath -am` 把实际路径绝对化并转为 Windows CMake 可识别的带盘符形式；它不负责下载或发现模块。

成功应输出包含当前安装根的 `Found toolchain: zephyr 1.0.1 (...)`，完成 `Configuring done` / `Generating done`，并在 `-B` 目录生成缓存与构建规则。若 SDK 已找到但报 CMSIS、模块或其他工具缺失，回到相应主机准备章或 P005，不把模块下载错误当成 SDK 错误。这里没有要求重复设置默认的工具链类型。

`-D` 的值保存在这个构建目录的 `CMakeCache.txt`，跨终端保留，不是“只对本条命令有效”。另一个新 `-B` 目录不会自动继承它。更换 SDK / 工具链时先用新目录验证；重配与清理策略在 [P012](../P012_CMake缓存与构建排错.md)，不为了本实验删除已有构建或改官方 `CMakeLists.txt`。

<a id="standalone-toolchain"></a>

## 2. 对照独立 ARM 工具链

独立 ARM 包须已按 [P004 的安装说明](../P004_SDK准备与编译器选型.md#standalone-toolchain)解压。

主机 CMake、Ninja 和 Python 仍是前提；`dtc` 用于补充设备树诊断，`gperf` 按所选功能使用，具体用途见 [P003 3.1.1](../P003_主机工具与Python环境_UCRT64.md#section-3-1-1)，不能一概当成每次构建的硬性条件。按 [P005 §5.3](../P005_源码依赖与离线准备.md#53_先核验文件再让配置过程确认发现结果) 完成 cmsis 与 cmsis_6 核验并完成 P008 的首次构建后，可以用同一官方应用、同一 `BOARD` 配置新的构建目录；这一工具链对照仍不需要 HC32 HAL：

```bash
# Windows UCRT64；P003 环境与 P005 两个 CMSIS 模块已准备；独立 ARM 包已解压，使用新构建目录。
(
set -e
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
unset ZEPHYR_SDK_INSTALL_DIR
test -f ../modules/hal/cmsis/zephyr/module.yml
test -f ../modules/hal/cmsis_6/CMSIS/Core/Include/core_cm4.h
MSYS2_ARG_CONV_EXCL='*' /ucrt64/bin/cmake \
  -S "$(cygpath -am samples/hello_world)" -B "$(cygpath -am build/learning-tools/p003/arm-standalone)" \
  -G Ninja -DBOARD=mps2/an386 \
  "-DZephyr_DIR=$(cygpath -am share/zephyr-package/cmake)" \
  "-DPYTHON_EXECUTABLE=$(cygpath -am .venv/Scripts/python.exe)" "-DPython3_EXECUTABLE=$(cygpath -am .venv/Scripts/python.exe)" \
  "-DCMAKE_MAKE_PROGRAM=$(cygpath -am /ucrt64/bin/ninja.exe)" \
  "-DZEPHYR_MODULES=$(cygpath -am ../modules/hal/cmsis);$(cygpath -am ../modules/hal/cmsis_6)" \
  -DZEPHYR_TOOLCHAIN_VARIANT=cross-compile \
  "-DCROSS_COMPILE=$(cygpath -am ../arm-zephyr-eabi/bin/arm-zephyr-eabi-)" \
  "-DCROSS_COMPILE_TOOLCHAIN_PATH=$(cygpath -am ../arm-zephyr-eabi)" \
  -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
)
```

**参数定位：上方代码块。** 行号从块内首行起算，注释和空行计入；自动折行不计。

<!-- parameter-lines:start -->
| 块内行号 | 原样参数片段 | 读取者与作用 |
| --- | --- | --- |
| 9 | `MSYS2_ARG_CONV_EXCL` | 本次关闭自动参数转换 |
| 10 | `-S` | 应用入口与独立构建目录 |
| 11 | `-G Ninja` | 选择 Ninja 与板目标 |
| 12 | `-DZephyr_DIR=` | 当前 Zephyr 源码包入口 |
| 13 | `-DPYTHON_EXECUTABLE=` | 两个 Python 接口指向同一 Windows venv |
| 14 | `-DCMAKE_MAKE_PROGRAM=` | 固定 UCRT64 Ninja |
| 15 | `-DZEPHYR_MODULES=` | 本例完整 CMSIS 模块列表，保持为一个参数 |
| 16 | `-DZEPHYR_TOOLCHAIN_VARIANT=` | 选择 cross-compile 规则 |
| 17 | `-DCROSS_COMPILE=` | 工具公共前缀 |
| 18 | `-DCROSS_COMPILE_TOOLCHAIN_PATH=` | 独立工具链根 |
| 19 | `-DCMAKE_EXPORT_COMPILE_COMMANDS=` | 生成编译命令数据库 |
<!-- parameter-lines:end -->

前面的 `unset` 只取消本操作子 shell 中的 SDK 根环境输入，不改变外层终端，也不删除 SDK 或用户包记录。选择新 `-B` 防止沿用另一条路线的缓存。输出应为 `Found toolchain: cross-compile (...)`，编译器指向独立 ARM 目录；若仍加载旧 SDK，核对当前环境和新目录选择。

`CROSS_COMPILE` 不是 `bin`，也不是完整的 `gcc.exe`。Zephyr 将 `gcc`、`g++`、`objcopy` 等程序名接到共同前缀后；目标库也必须与工具链一起保留。独立路线由读者选定工具链，改 `BOARD` 不会自动换成另一种架构的工具。实际编译替代实验见 [P015](../P015_新增开发板与芯片支持.md#standalone-toolchain)；原生机制见 [Other Cross Compilers](https://docs.zephyrproject.org/latest/develop/toolchains/other_x_compilers.html)。

<a id="sdk-evidence"></a>

## 3. 从配置产物确认所选工具

前面的 GCC 版本检查只证明程序可运行。执行本页第 1 节的配置后，CMake 会在该命令 `-B` 指定的 `/g/zephyr_practice/zephyr-main/build/learning-tools/p003/sdk-explicit` 中生成配置记录。下面先进入这个目录，再读取同级的 `CMakeCache.txt`、`compile_commands.json` 和子目录中的 `zephyr/.config`；这三份文件不是 SDK 安装包里的文件，也不是准备阶段就应存在的输入：

```bash
# Windows UCRT64；源码依赖齐全且 本页第 1 节的 CMake 配置成功后，才有这些产物。
cd /g/zephyr_practice/zephyr-main/build/learning-tools/p003/sdk-explicit
grep -E 'ZEPHYR_SDK_INSTALL_DIR|CMAKE_C_COMPILER' CMakeCache.txt
grep -m1 'arm-zephyr-eabi-gcc' compile_commands.json
grep -E '^CONFIG_(ARCH|CPU_CORTEX_M4|FPU|ARM)' zephyr/.config
```

缓存应指向本次 SDK 根及其 `gnu/arm-zephyr-eabi` 下的 GCC；`compile_commands.json` 包含计划执行的编译命令和目标参数；`zephyr/.config` 记录板 / SoC 配置。若执行的是 本页第 2 节的独立工具链配置，把查看位置换为 `/g/zephyr_practice/zephyr-main/build/learning-tools/p003/arm-standalone`，再读取相同的三个相对路径，对照独立工具链前缀。`compile_commands.json` 可以在生成阶段产生，不证明命令已经执行；实际构建、固件和 QEMU 运行继续在 P008 / P015 验证。

配套命令索引中标为“构建后参考”的条目对应本页：[SDK 命令索引](../commands/current/P004_SDK准备与编译器选型/README.md)。
