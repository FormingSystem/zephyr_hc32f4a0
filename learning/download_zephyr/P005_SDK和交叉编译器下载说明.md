---
id: zephyr-download-notes-05
title: 从 Zephyr 源码版本选择 SDK、下载 ARM 工具链并完成编译
kind: engineering
status: evolving
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第5章\_从\_Zephyr\_源码版本选择\_SDK、下载\_ARM\_工具链并完成编译

当前型号与依赖依据统一见[准备专题 P004 的 4.1 节](../P01_zephyr_make_project/环境与依赖导航.md#chip-selection)，完整下载和核验见[准备专题 P004 的 4.2.2、4.2.3 节](../P01_zephyr_make_project/P004_CMSIS与HAL选择下载_Windows.md#section-4-2)。实装芯片先用丝印/BOM/手册确认；CMSIS_6 版本来自当前 Zephyr 清单，HC32 HAL 来自配套移植指定的 hal_xhsc 快照。当前官方清单没有 hal_xhsc，AN386 编译示例也不需要它。下文其他模块名称与布局示例不能替代这条实际操作路线。

上一章已经取得 Zephyr 源码和配套模块。现在先用原生 MPS2 目标把 C 程序编译成 ARM 固件，为后续 HC32 适配验证工具环境，读者还需要建立三条联系：**源码版本决定采用哪版 SDK；SDK 发布决定其中的编译器版本；芯片架构决定选用其中哪一套工具链。** 三条联系成立后，还要把路径和板级目标交给构建系统，不能以“下载完了”作为开发环境准备完成的标志。

SDK 是 Software Development Kit，即软件开发工具包，本章具体指 Zephyr 发行的开发工具包。ARM 是芯片的处理器架构家族；GCC 是 GNU Compiler Collection，即 GNU 编译器集合。三个名称分别描述工具集合、目标架构和编译器，不属于同一层。

本章从读者解压的 **原生 Zephyr** 查依据，操作环境为 **Windows x64 + MSYS2 UCRT64 Bash**。2026-10-03 核对的原生源码为 4.5.0-rc1，提交 `3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4`。本文中的原生文件链接固定到该修订，读者可在自己的解压根目录打开同一路径；实验在 `G:\zephyr_practice\zephyr-main` 进行。

本章统一使用原生 `mps2/an386` 目标：5.1 确认版本，5.2 解释 ARM 架构映射，5.3 下载 SDK，5.4 准备依赖与自建应用，5.5—5.6 配置、编译并反查结果，5.7 用原生 hello_world 交叉验证。这份上游源码没有 HC32/UYUP 支持，HC32 移植是后续工作。

| 要确认的对象 | 这份原生源码的结果 | 原生依据 |
| --- | --- | --- |
| Zephyr 源码版本 | 4.5.0-rc1 | [VERSION](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/VERSION) |
| 默认安装的 SDK 版本 | 1.0.1 | [SDK_VERSION](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/SDK_VERSION)；[sdk.py](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/scripts/west_commands/sdk.py)默认读取此文件 |
| 文档下载链接怎样得到版本 | doc/conf.py 读取 SDK_VERSION，生成 sdk-version 与下载 URL | [doc/conf.py](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/doc/conf.py#L67) |
| CMake 怎样判定兼容 | 请求 Zephyr-sdk 1.0，并让 SDK 包版本配置参与判断 | [FindHostTools.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/cmake/modules/FindHostTools.cmake#L51) |
| GCC 版本 | SDK 1.0.1 中 GCC 14.3.0，带 Zephyr 补丁 | [SDK 官方发布组件清单](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v1.0.1) |
| 32 位 ARM 工具链 | arm-zephyr-eabi | 原生 [toolchain/zephyr/target.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/cmake/toolchain/zephyr/target.cmake)加载 [SDK GNU target.cmake](https://github.com/zephyrproject-rtos/sdk-ng/blob/v1.0.1/cmake/zephyr/gnu/target.cmake) |
| 原生演示目标 | mps2/an386 | [board.yml](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/boards/arm/mps2/board.yml)和 [SoC Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/soc/arm/mps2/Kconfig) |

**阅读与操作路线**

```text
① 查源码、SDK、GCC 的版本依据 → ② 从芯片找到工具链
  → ③ 下载、校验和安装 → ④ 准备应用与主机依赖
  → ⑤ 配置源码、模块、SDK 和 BOARD → ⑥ 编译与反查结果
  → ⑦ 换成官方 ZIP、换芯片或继续开发
```

- [5.1 实验源码怎样对应 SDK 和编译器版本](#section-5-1)
- [5.2 HC32F4A0 怎样对应 ARM 工具链](#section-5-2)
- [5.3 官方下载入口、校验和安装](#section-5-3)
- [5.4 建立自己的应用和主机环境](#section-5-4)
- [5.5 工程怎样发现 SDK 和交叉编译器](#section-5-5)
- [5.6 编译并检查实际使用的版本与目标](#section-5-6)
- [5.7 官方 ZIP、其他芯片和后续开发](#section-5-7)

**本章导航**

- [5.1 实验源码怎样对应 SDK 和编译器版本](#section-5-1)
- [5.2 HC32F4A0 怎样对应 ARM 工具链](#section-5-2)
- [5.3 官方下载入口、校验和安装](#section-5-3)
- [5.4 建立自己的应用和主机环境](#section-5-4)
- [5.5 工程怎样发现 SDK 和交叉编译器](#section-5-5)
- [5.6 编译并检查实际使用的版本与目标](#section-5-6)
- [5.7 官方 ZIP、其他芯片和后续开发](#section-5-7)

<a id="section-5-1"></a>

## 5.1\_实验源码怎样对应\_SDK\_和编译器版本

**当前步骤：① 版本依据。** 进入自己解压的原生源码，确认直接包含 VERSION 和 SDK_VERSION。下面输入目录时不加引号；`cygpath` 将 Windows 目录转换为 Bash 能使用的路径。

### 5.1.1\_源码版本、默认安装版本与兼容检查

```bash
# 将 Zephyr 解压根目录做出系统变量，后续方便跳转定位该位置，执行对应的命令。这里输入windows路径类型
read -r -p 'Zephyr 解压目录：' ZEPHYR_SOURCE_INPUT

# 把windows路径换成linux路径
cd "$(cygpath -u "$ZEPHYR_SOURCE_INPUT")"

pwd
cat VERSION
cat SDK_VERSION
```

本次原生 VERSION 中主版本 4、次版本 5、补丁 0 和扩展 rc1 合成 **4.5.0-rc1**；SDK_VERSION 为 **1.0.1**。两者是不同项目的编号，没有数字换算公式。ZIP 目录名也不决定版本；若 ZIP 没有 `.git`，不能要求读者必须运行 git describe，应记录下载来源和修订并读取这些原生文件。

上述命令执行示例：

```bash
Lizha@lizhaojun UCRT64 /g/zephyr-main/zephyr-main
$ read -r -p 'Zephyr 解压目录：' ZEPHYR_SOURCE_INPUT
Zephyr 解压目录：G:\zephyr-main\zephyr-main

Lizha@lizhaojun UCRT64 /g/zephyr-main/zephyr-main
$ cd "$(cygpath -u "$ZEPHYR_SOURCE_INPUT")"
pwd
cat VERSION
cat SDK_VERSION
/g/zephyr-main/zephyr-main
VERSION_MAJOR = 4
VERSION_MINOR = 5
PATCHLEVEL = 0
VERSION_TWEAK = 0
EXTRAVERSION = rc1
1.0.1
```

SDK_VERSION 的意义可以沿两条原生代码路径确认。第一条是 `scripts/west_commands/sdk.py`：`west sdk install` 未传 `--version` 时读取该文件。第二条是 `doc/conf.py`：读取同一个文件，并把版本替换进 `doc/develop/toolchains/zephyr_sdk.rst` 的安装文本与 SDK 下载 URL。该原生说明把文档所引用版本称为对应 Zephyr 的推荐版本，并链接官方兼容矩阵。手工下载应沿同一条来源链，而不是根据芯片型号猜版本。

再打开 `cmake/modules/FindHostTools.cmake`，可以看到 `find_package(Zephyr-sdk 1.0)`。**这是构建时的兼容请求，不是默认下载命令，也没有写 EXACT 1.0.1。** 后续 `FindZephyr-sdk.cmake` 与 SDK 自带包版本文件一起判断候选是否兼容。SDK_VERSION=1.0.1 不能解释成 CMake 只允许这一版，1.0 的兼容请求也不能解释成任意未来 SDK 必然可用。

原生说明的完整入口是 [zephyr_sdk.rst](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/doc/develop/toolchains/zephyr_sdk.rst)，它指向 [SDK 版本兼容矩阵](https://github.com/zephyrproject-rtos/sdk-ng/wiki/Zephyr-Version-Compatibility#zephyr-sdk-version-compatibility-matrix)。该在线矩阵会更新；讲旧源码时优先看所下载修订的文件，再对照矩阵，不用 latest 页面替旧工程决定版本。

### 5.1.2\_SDK\_发布怎样连接到\_GCC\_版本

原生仓库没有一张“HC32F4A0 → GCC 14.3.0”的表。本例能查证的是间接关系：

```text
原生 Zephyr 4.5.0-rc1 的 SDK_VERSION = 1.0.1
  → SDK 官方 v1.0.1 Release 的 Included Components
  → GCC 14.3.0（含 Zephyr 补丁）
  → 按目标架构选择其中的 arm-zephyr-eabi 发行附件
```

打开 [SDK 1.0.1 发布页](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v1.0.1)，在 **Included Components → Toolchains** 查询 GCC 14.3.0、Binutils 2.43.1 和 GDB 16.2。Binutils 提供汇编、链接和目标文件处理工具，GDB 用于调试。发布清单给出包内组件版本；安装后的 `arm-zephyr-eabi-gcc.exe --version` 则检查本机真正拿到的文件。

这条链只说明选择这个官方 SDK 发布会得到什么编译器组合。它不是每个 Zephyr 版本唯一对应一个 GCC 的定律，也不能据此把另一份同主版本的 arm-none-eabi-gcc 随意替换进来：补丁、目标库和 CMake 接入结构都可能不同。

### 5.1.3\_先保存源码位置，再建立下载目录

保持使用 `G:\zephyr_practice\zephyr-main`。下面用自定变量 `SOURCE_ROOT` 保存 Bash 源码路径，`SOURCE_ROOT_WIN` 保存 Windows 程序可读取的形式，`SDK_RELEASE` 从源码版本文件读取：

`PWD` 是 Bash 提供的当前位置变量，`cygpath` 是 MSYS2 的路径转换命令。本章始终读取这些位置，不修改其他工程的配置。

变量提示：以下名称均为**教程自定义的临时 Bash 变量，不是 Zephyr 或 CMake 原生接口**。

- `SOURCE_ROOT`：定义见 5.1.3 先保存源码位置，再建立下载目录；该实验源码根的 Bash 路径。
- `SOURCE_ROOT_WIN`：定义见 5.1.3 先保存源码位置，再建立下载目录；该实验源码根的 Windows 路径。
- `SDK_RELEASE`：定义见 5.1.3 先保存源码位置，再建立下载目录；从 SDK_VERSION 读取的发行号。

```bash
# 当前位置：任意目录；终端：UCRT64。
cd /g/zephyr_practice/zephyr-main
SOURCE_ROOT="$PWD"
SOURCE_ROOT_WIN="$(cygpath -m "$SOURCE_ROOT")"
SDK_RELEASE="$(tr -d '\r\n' < "$SOURCE_ROOT/SDK_VERSION")"
mkdir -p "$SOURCE_ROOT/build/learning-tools/sdk-p05/downloads/sdk"
cd "$SOURCE_ROOT/build/learning-tools/sdk-p05"
printf '源码：%s\nSDK：%s\n' "$SOURCE_ROOT_WIN" "$SDK_RELEASE"
```

`cygpath -m` 转成盘符加正斜杠的 Windows 路径；`tr` 去掉版本文件末尾的换行。输出应是 `G:/zephyr_practice/zephyr-main` 与 `1.0.1`。本章应用和下载缓存保存在这个源码目录的 `build/learning-tools/sdk-p05` 下；SDK 安装目录仍可单独选择。

这些变量只在当前终端有效。中途重新开终端时，需重新定位源码并设置变量，不能假定进入目录就自动恢复了环境。

<a id="section-5-2"></a>

## 5.2\_HC32F4A0\_怎样对应\_ARM\_工具链

**当前步骤：① → ② 芯片与工具链。** 已经选定 SDK 发布版本，接下来才判断这个 SDK 中要用哪一个目标工具链。这一步看芯片架构，不再靠比较 SDK 版本号猜测。

### 5.2.1\_先检查原生仓库是否支持该芯片

先在所下载的原生源码中检查 `boards/` 与 `soc/`。本次原生快照中没有 HC32F4A0/UYUP，因而不能从上游找到它的 board.yml，也不存在官方 HC32 专属 SDK 下载项。原生可查的 Cortex-M4 例子是 [soc/arm/mps2/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/soc/arm/mps2/Kconfig)：SOC_SERIES_MPS2 选择 ARM，SOC_AN386 选择 CPU_CORTEX_M4。它证明原生架构选择机制，不证明 HC32 硬件适配已完成。

Kconfig 是 Zephyr 的配置系统。上述原生 MPS2 配置中的 `ARM` 和 `CPU_CORTEX_M4` 决定架构与处理器核，构建据此选择 32 位 ARM 编译工具与 CPU 参数。HC32F4A0 也采用 Cortex-M4F，但相同处理器核不代表相同外设、时钟或存储布局。因此可以选用同一工具链家族，却不能直接使用 MPS2 固件运行 HC32。

SDK 版本仍由源码推荐版本与兼容要求决定，不能从芯片型号直接算出 SDK/GCC 版本。

### 5.2.2\_从\_ARM\_配置追到具体工具链前缀

选择 Zephyr SDK 后，原生 [cmake/toolchain/zephyr/target.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/cmake/toolchain/zephyr/target.cmake) 会加载 SDK 内的 GNU 工具链配置。SDK 1.0.1 的 [cmake/zephyr/gnu/target.cmake](https://github.com/zephyrproject-rtos/sdk-ng/blob/v1.0.1/cmake/zephyr/gnu/target.cmake)中有这层映射：

| Zephyr 最终架构选择 | SDK 中的工具链目标 | 本章是否使用 |
| --- | --- | --- |
| 32 位 ARM，即本例的 ARM/Cortex-M4 | arm-zephyr-eabi | 是 |
| ARM64 | aarch64-zephyr-elf | 否 |
| RISC-V | riscv64-zephyr-elf | 否，换架构时重新核对 |

SDK 配置先按 `ARCH` 得到目标前缀，再拼出 `SDK根/gnu/arm-zephyr-eabi/bin/arm-zephyr-eabi-`。GCC、G++、objcopy、readelf 等工具共享这个前缀。`eabi` 是 Embedded Application Binary Interface，即嵌入式应用二进制接口，约定二进制调用等规则；它不是 HC32 的芯片编号。

原生 `boards/arm/mps2/board.yml` 将 `mps2` 与 `an386` 关联，得到本章构建目标 `mps2/an386`。具体 CPU、内存和外设由该板与 SoC 配置决定。

### 5.2.3\_主机架构和目标架构怎样合成下载条件

现在已经知道：SDK 发布为 1.0.1，目标工具链为 `arm-zephyr-eabi`，而编译器本身要在 Windows x64 电脑上运行。因此独立工具链附件是：

```text
toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z
              └─运行在电脑上─┘ └─生成目标代码─┘
```

文件名同时含 x86-64 和 ARM 很正常，它们分别描述编译器的运行平台和输出平台。UCRT64 是 Windows 上的终端与工具环境，使用 Bash 不会把电脑变成 Linux，因此不能下载 Linux 工具链包来运行。

到这里，读者应能沿源码找到下载条件，而不只是记住一个文件名：**原生 SDK_VERSION 选推荐发布版，SoC Kconfig 与 SDK target.cmake 选目标家族，Windows 电脑选主机平台。**

<a id="section-5-3"></a>

## 5.3\_官方下载入口、校验和安装

**当前步骤：① → ② → ③ 下载安装。** 三个条件已经明确，现在到具体发布页取得文件。本节选 Minimal SDK 加单独 ARM 工具链，完整 GNU Bundle 作为已有下载的替代路线。

### 5.3.1\_浏览器具体打开哪里、点击什么

打开 [Zephyr SDK 1.0.1 官方发布页](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v1.0.1)。这是 **sdk-ng** 仓库；下载操作系统源码的 **zephyr** 仓库是另一个入口。

在发布页 **Downloads** 区域按下表查找，底部 **Assets** 也能按文件名定位。三个文件都保存到前面创建的 `downloads/sdk/`：

| 所需文件 | 发布页位置 | 直接下载 |
| --- | --- | --- |
| zephyr-sdk-1.0.1_windows-x86_64_minimal.7z | SDK Bundle 表，Windows 行、Minimal 列的 x86-64 | [Minimal SDK](https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v1.0.1/zephyr-sdk-1.0.1_windows-x86_64_minimal.7z) |
| toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z | GNU Toolchains 表，arm-zephyr-eabi 行、Windows 列的 x86-64 | [ARM 工具链](https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v1.0.1/toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z) |
| sha256.sum | Assets 中的同名文件 | [官方 SHA-256 清单](https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v1.0.1/sha256.sum) |

**独立工具链附件名没有 SDK 版本号，但下载 URL 中有 `/v1.0.1/`。** 必须从同一发布版取得两个包和摘要，不能把其他版本的同名 ARM 工具链放进来。

Minimal 不带目标编译器，提供 SDK 基础目录与接入文件等内容；GNU Bundle 已包含各目标 GNU 工具链；LLVM Bundle 采用另一套编译器。本章只需这一区分。若已经取得同版 `zephyr-sdk-1.0.1_windows-x86_64_gnu.7z`，直接用它即可，不必重新下载 Minimal 与 ARM 两包。

不要选择页面底部的 `Source code (zip)` 来代替这些附件，那是制作 SDK 的工程源码，不是已经编译好的 Windows 工具。网络故障时先按[代理配置](代理配置.md)核对浏览器和 curl 下载通道；Git 的代理设置不会自动替浏览器下载配置代理。

### 5.3.2\_用命令下载并核对内容

如果希望直接从终端下载，下面可替代浏览器操作，不需要两种方式都执行：

变量提示：以下名称均为**教程自定义的临时 Bash 变量，不是 Zephyr 或 CMake 原生接口**。

- `SDK_RELEASE`：定义见 5.1.3 先保存源码位置，再建立下载目录；从 SDK_VERSION 读取的发行号。
- `SDK_URL`：定义见 5.3.2 用命令下载并核对内容；按发行号组成的官方下载 URL。

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；SDK_RELEASE 从实验源码读出，应为 1.0.1。
SDK_URL="https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v${SDK_RELEASE}"
curl -fL --retry 3 "$SDK_URL/zephyr-sdk-${SDK_RELEASE}_windows-x86_64_minimal.7z" \
  -o "downloads/sdk/zephyr-sdk-${SDK_RELEASE}_windows-x86_64_minimal.7z"
curl -fL --retry 3 "$SDK_URL/toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z" \
  -o downloads/sdk/toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z
curl -fL --retry 3 "$SDK_URL/sha256.sum" -o downloads/sdk/sha256.sum
```

`-L` 跟随 GitHub 下载跳转，`-f` 将 HTTP 错误作为失败返回，`--retry 3` 重试临时失败，`-o` 指定保存位置。任一下载失败时先修复网络，不继续解压。若源码要求的 SDK 不是 1.0.1，要重新核对该版的附件与目录布局，不只替换 URL 后照搬本文。

SHA-256 是文件摘要算法。只运行 `sha256sum 文件` 得到本地摘要还不够，要与官方同名条目比较：

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；本段按 Minimal + ARM 两包路线检查。
(
  cd downloads/sdk || exit 1
  # 当前位置：downloads/sdk；子 shell 结束后回到实验根。
  grep -E ' (zephyr-sdk-1\.0\.1_windows-x86_64_minimal\.7z|toolchain_gnu_windows-x86_64_arm-zephyr-eabi\.7z)$' \
    sha256.sum > selected.sha256
  test "$(wc -l < selected.sha256)" -eq 2 && sha256sum -c selected.sha256
)
```

应看到两个文件都输出 `OK`。`grep` 选出本次文件，`test` 防止漏选，`-c` 检查文件是否存在、摘要是否相等。若失败，重新取得对应附件再检查。GNU Bundle 路线则只选 GNU 包那一项核对，不拿它与 Minimal 的摘要比较。

### 5.3.3\_正确组合\_SDK\_根与工具链目录

先按[环境与目录约定](环境与目录约定.md)安装 7-Zip 和 CMake。已经有可用 SDK 的读者可以直接使用它，跳到身份检查，不要向未知旧目录叠加解压。首次安装时先看归档顶层：

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；7z l 只列内容。
7z l downloads/sdk/zephyr-sdk-1.0.1_windows-x86_64_minimal.7z
7z l downloads/sdk/toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z
```

Minimal 包带有顶层 `zephyr-sdk-1.0.1/`，独立工具链带有 `arm-zephyr-eabi/`。所以前者解到实验根，后者解到 SDK 内的 `gnu/`：

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；首次安装，zephyr-sdk-1.0.1 尚不存在。
7z x downloads/sdk/zephyr-sdk-1.0.1_windows-x86_64_minimal.7z -o.
mkdir -p zephyr-sdk-1.0.1/gnu
7z x downloads/sdk/toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z \
  -ozephyr-sdk-1.0.1/gnu
```

GNU Bundle 路线把上面三行换成 `7z x downloads/sdk/zephyr-sdk-1.0.1_windows-x86_64_gnu.7z -o.`。安装完成后，两条路线都应包含：

```text
zephyr-sdk-1.0.1/
├── sdk_version
├── setup.cmd
├── cmake/
├── hosttools/
└── gnu/arm-zephyr-eabi/
    ├── bin/arm-zephyr-eabi-gcc.exe
    ├── bin/arm-zephyr-eabi-readelf.exe
    └── arm-zephyr-eabi/              目标头文件和运行库等
```

后面设置 SDK 路径时，要指向含 `sdk_version` 的根目录，不是 `gnu/` 或 `bin/`。SDK 可以独立放置并被多个工程使用，不必复制进 Zephyr 解压目录。

### 5.3.4\_在 PowerShell 执行 Windows SDK 安装脚本

这一段切换到 **Windows PowerShell**。这里调用 Windows 专用的 setup.cmd，所以切换终端；下载、摘要、解压和后续工程操作仍默认使用 UCRT64。按本章前面的解压位置进入 SDK 根，已有 ARM 目录时安装脚本会跳过下载。

```powershell
# Windows PowerShell；本章 SDK 已解压，CMake 与 7-Zip 已安装。
Set-Location -LiteralPath 'G:\zephyr_practice\zephyr-main\build\learning-tools\sdk-p05\zephyr-sdk-1.0.1'
.\setup.cmd /t arm-zephyr-eabi
# 完成 Windows 脚本操作后，回到 UCRT64 做下面的工具检查。
```

下面切回 **UCRT64**，重新进入本章 SDK 根；PowerShell 的当前位置不会传给 Bash。

```bash
# UCRT64；本章的 SDK 安装已完成，按实际位置调整 cd。
cd /g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05/zephyr-sdk-1.0.1
cat sdk_version
./gnu/arm-zephyr-eabi/bin/arm-zephyr-eabi-gcc.exe --version
./gnu/arm-zephyr-eabi/bin/arm-zephyr-eabi-gcc.exe -dumpmachine
```

应分别确认 SDK 1.0.1、GCC 14.3.0、目标 arm-zephyr-eabi。`/t` 安装指定目标工具链；可选的 `.\setup.cmd /c` 将 SDK 的 cmake 地址保存到当前 Windows 用户的 CMake 包注册表，跨终端保留，供多个工程自动查找。本章使用显式 SDK 路径，不要求执行 `/c`。`/h` 在 Windows 1.0.1 的脚本中跳过，不能据此认定安装了 QEMU。

依据：[SDK 1.0.1 Windows 安装脚本](https://github.com/zephyrproject-rtos/sdk-ng/blob/v1.0.1/scripts/template_setup_win)。下一节继续在 UCRT64，按其注释重新进入实验目录；PowerShell 的当前目录不会传到另一个终端。实际工程采用哪个 SDK，要在 5.6 核对。

<a id="section-5-4"></a>

## 5.4\_建立自己的应用和主机环境

**当前步骤：③ → ④ 应用与依赖。** SDK 已具备编译器、链接器和目标运行库，还需要由主机工具读取工程并组织调用。CMake 生成构建规则，Ninja 执行规则，Python 执行 Zephyr 的配置及代码生成脚本，DTC 处理设备树，gperf 用于部分代码生成。

### 5.4.1\_准备执行构建的工具

主机工具统一按[Windows 主线安装说明](../P01_zephyr_make_project/环境与依赖导航.md)处理：先在 PowerShell 使用官方 winget 包清单，再重开 UCRT64 核对 `type -a cmake ninja dtc gperf 7z`。Python 采用已核对的 Windows CPython 3.12.10；有 Launcher 时使用 `py -3.12`，没有时按主线定位 `python.exe`。工具来源及 Linux 分支见[官方依据](../P01_zephyr_make_project/主机工具与官方安装来源.md)。

变量提示：以下名称均为**教程自定义的临时 Bash 变量，不是 Zephyr 或 CMake 原生接口**。

- `SOURCE_ROOT`：定义见 5.1.3 先保存源码位置，再建立下载目录；该实验源码根的 Bash 路径。
- `SOURCE_ROOT_WIN`：定义见 5.1.3 先保存源码位置，再建立下载目录；该实验源码根的 Windows 路径。

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；首次创建本实验 .venv，已有则只激活。
py -3.12 -m venv "$SOURCE_ROOT_WIN/.venv"
source "$SOURCE_ROOT/.venv/Scripts/activate"
python -c 'import sys; print(sys.executable); print(sys.platform)'
python -m pip install -r "$SOURCE_ROOT_WIN/scripts/requirements-base.txt"
python -m pip check
```

`venv` 创建独立的 Python 环境；输出应指向本实验 `.venv/Scripts/python.exe`，平台为 `win32`，包括 64 位 Windows。`python -m pip` 安装到这个解释器。这里读取原生源码的 `scripts/requirements-base.txt`，环境位于实验源码根的 `.venv`。已有该环境时跳过创建，只激活和核对依赖。

已有工程 `.venv` 的读者也可在新终端使用该环境与本章的独立应用，但需确认实际解释器和 PATH。完整的隔离、离线包和环境维护方法在 P006；本章不把 Python 依赖当成 SDK 的组成部分。

### 5.4.2\_复用 west 管理的 CMSIS

本章使用官方 mps2/an386。CMSIS 的仓库、修订和目录由当前源码 west.yml 决定；按 [P004 的 4.2 节](../P01_zephyr_make_project/P004_CMSIS与HAL选择下载_Windows.md#section-4-2) 在同一源码上建立工作区并取得模块。无需在 SDK 实验目录再下载一份 ZIP。Git for Windows 的选择也沿用 P002 的 2.1.1。

```bash
# Windows UCRT64；当前位置：源码根/build/learning-tools/sdk-p05；.venv 已激活。
# 此目录位于 主线 P004 已核对的同一个 west 工作区内。
west topdir
west list cmsis_6 -f '{url} {revision} {abspath}'
west update cmsis_6
west forall cmsis_6 -c 'git rev-parse HEAD'
```

模块位于工作区根/modules/hal/cmsis_6，由 west 生成 Git 仓库并检出清单提交。SDK 是主机工具，CMSIS 是源码依赖；直接使用 CMake 时，Zephyr 仍可通过 west 找到模块，不必指定 CMSIS 路径。

### 5.4.3\_建立一个可编译的应用

应用放在实验目录的 `app/`；先确认这里没有需要保留的同名应用。`CMakeLists.txt` 与 `prj.conf` 是构建约定文件，`sdk_probe` 是本例自行选择的工程名。

文件中的 `ZEPHYR_BASE` 是稍后要设置的源码根环境变量，CMake 用 `$ENV{...}` 读取它；`HINTS` 提供查找提示，`REQUIRED` 要求找不到 Zephyr 时停止。`PRIVATE` 表示该源文件属于当前构建目标，`CONFIG_PRINTK` 是启用打印的 Kconfig 配置项。`EOF` 只是本段文件输入的结束标记。

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；首次建立本章 app，目标文件尚不存在。
mkdir -p app/src
cat > app/CMakeLists.txt <<'EOF'
cmake_minimum_required(VERSION 3.20.0)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(sdk_probe)
target_sources(app PRIVATE src/main.c)
EOF
cat > app/prj.conf <<'EOF'
CONFIG_PRINTK=y
EOF
cat > app/src/main.c <<'EOF'
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>

int main(void)
{
    printk("SDK mapping OK\n");
    return 0;
}
EOF
```

带单引号的 `<<'EOF'` 原样写入文件，不让 Bash 提前展开 CMake 的 `$ENV{ZEPHYR_BASE}`。`find_package` 引入 Zephyr 构建逻辑，`project` 声明工程，`target_sources` 将 `main.c` 加入 Zephyr 的 `app` 构建目标。`CONFIG_PRINTK` 启用打印函数，运行固件时才会输出这行文字；编译阶段不会产生串口输出。

完成后，源码仍在实验源码目录，实验目录中有 SDK 下载缓存和 app，CMSIS 位于 west 工作区的模块目录，Python 环境位于源码根 .venv；`build-mps2-west/` 尚未生成。下面通过 CMake 把它们连接起来。

<a id="section-5-5"></a>

## 5.5\_工程怎样发现\_SDK\_和交叉编译器

**当前步骤：④ → ⑤ 配置关联。** 解压行为不会自动让某个工程认领 SDK。真正建立关联的是 CMake 配置阶段：给它源码位置、模块列表、SDK 根和板级目标，它据此生成构建规则。

### 5.5.1\_设置明确的路径

变量提示：以下名称均为**教程自定义的临时 Bash 变量，不是 Zephyr 或 CMake 原生接口**。

- `SOURCE_ROOT_WIN`：定义见 5.1.3 先保存源码位置，再建立下载目录；该实验源码根的 Windows 路径。
- `PYTHON_EXE`：定义见 5.5.1 设置明确的路径；当前已激活 venv 的解释器路径。

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；已激活本实验 .venv。
export ZEPHYR_BASE="$SOURCE_ROOT_WIN"
export ZEPHYR_SDK_INSTALL_DIR="$(cygpath -m "$PWD/zephyr-sdk-1.0.1")"
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
unset ZEPHYR_MODULES EXTRA_ZEPHYR_MODULES ZEPHYR_EXTRA_MODULES
PYTHON_EXE="$(python -c 'import sys; print(sys.executable.replace(chr(92), "/"))')"
```

如果 SDK 已安装在别处，只将 `ZEPHYR_SDK_INSTALL_DIR` 改为 **实际含 sdk_version 的目录**，并用 `cygpath -m` 转换路径；不必再复制一份 SDK。

| 变量 | 含义 | 后续消费者 |
| --- | --- | --- |
| ZEPHYR_BASE | 当前源码根 | Zephyr 构建逻辑寻找内核、boards、Kconfig 和脚本 |
| ZEPHYR_SDK_INSTALL_DIR | SDK 安装根 | SDK 查找与工具链配置 |
| ZEPHYR_TOOLCHAIN_VARIANT | zephyr，采用 Zephyr SDK 的接入方式 | CMake 选择 toolchain 配置逻辑 |
| PYTHON_EXE | 当前虚拟环境的解释器 | 下一条命令选择 Python 执行者 |

`export` 只把变量传给当前 Bash 后续启动的子进程，不会永久修改 Windows 设置。Windows 原生程序读取盘符路径，因此这里不用 `/f/...` 形式的环境变量值。

### 5.5.2\_生成构建规则

变量提示：以下名称均为**教程自定义的临时 Bash 变量，不是 Zephyr 或 CMake 原生接口**。

- `PYTHON_EXE`：定义见 5.5.1 设置明确的路径；当前已激活 venv 的解释器路径。

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；第一次配置使用新的 build-mps2-west。
cmake -S app -B build-mps2-west -G Ninja \
  -DBOARD=mps2/an386 \
  "-DZephyr_DIR=$ZEPHYR_BASE/share/zephyr-package/cmake" \
  "-DZEPHYR_BASE=$ZEPHYR_BASE" \
  "-DZEPHYR_SDK_INSTALL_DIR=$ZEPHYR_SDK_INSTALL_DIR" \
  -DZEPHYR_TOOLCHAIN_VARIANT=zephyr \
  -DEXTRA_ZEPHYR_MODULES= -DZEPHYR_EXTRA_MODULES= \
  "-DPython3_EXECUTABLE=$PYTHON_EXE" \
  -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```

`-S` 指定应用目录，`-B` 指定配置和编译输出位置，`-G Ninja` 选择执行构建规则的工具；`-D名字=值` 将设置交给 CMake，并在构建目录缓存。

`Zephyr_DIR` 指向当前源码的 CMake 包入口，`ZEPHYR_BASE` 指向源码根。两者同时明确指定，可避免机器上登记过的另一份 Zephyr 被选中。`BOARD` 是本板的真实目标，不是随意填写芯片名。

本例不设置 ZEPHYR_MODULES，由 west 提供已下载模块的位置。配置前清除遗留模块环境变量，并使用新的构建目录，避免旧显式列表覆盖自动发现。工作区初始化和下载已在 P002 完成，CMake 不会替你联网补齐缺少的模块。

`Python3_EXECUTABLE` 选用刚才核对的解释器；最后一个参数生成编译数据库 `compile_commands.json`，供下一节查看真实命令。配置成功应显示实验源码路径、mps2/an386 目标、SDK 1.0.1、GNU 14.3.0，并在 `build-mps2-west/` 生成规则。

### 5.5.3\_同名变量有三种存放位置

“CMake 环境变量”容易把不同对象混在一起。先看值存在哪里，再看哪段代码读取它。下面的变量名 `SDK_PATH` 只是帮助理解的自定名字，不是 Zephyr 接口。

| 写法与执行者 | 值存在哪里 | 有效时间与读取方式 |
| --- | --- | --- |
| Bash：`SDK_PATH=...` | 当前 shell 的普通变量 | 当前 shell 可用；`$SDK_PATH` 由 Bash 展开，不会自动传给子进程 |
| Bash：`export ZEPHYR_SDK_INSTALL_DIR=...` | 当前进程环境，并由之后启动的子进程继承 | CMake 用 `$ENV{ZEPHYR_SDK_INSTALL_DIR}` 读取；关闭终端后不保留这次 export |
| 命令行：`cmake -D名字=值 ...` | 所选构建目录的 CMake 缓存 | 配置成功后保存在 `CMakeCache.txt`，下次配置仍可用；不是 Windows 全局环境 |
| CMake 脚本：`set(名字 值)` | CMake 普通变量作用域 | `${名字}` 读取；目录、函数等作用域会影响可见性，不会因为 set 就写入缓存 |
| CMake 脚本：`set(名字 值 CACHE STRING "说明")` | CMake 缓存 | 通常保留已有缓存值；`FORCE` 可以强制改写，须看调用者代码 |

例如 Bash 中的 `"-DZEPHYR_SDK_INSTALL_DIR=$ZEPHYR_SDK_INSTALL_DIR"` 分两步执行：Bash 先把右侧 `$...` 换成路径；CMake 收到的是已经展开的 `-DZEPHYR_SDK_INSTALL_DIR=盘符:/目录`，再建立同名缓存项。左右名称相同只是便于阅读，并不表示 CMake 把全部环境变量自动转换成了普通变量。

在 CMake 文件中，`${名字}` 通常先找普通变量、再找缓存；`$CACHE{名字}` 明确读取缓存；`$ENV{名字}` 明确读取进程环境。**这只是 CMake 的基本查值规则，Zephyr 的辅助函数可以另行规定选择顺序。** [CMake 变量说明](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variables)解释这些独立存储空间。

### 5.5.4\_Zephyr\_怎样处理环境与缓存冲突

原生源码 `cmake/modules/FindZephyr-sdk.cmake` 先调用 `zephyr_get(ZEPHYR_TOOLCHAIN_VARIANT)`、`zephyr_get(ZEPHYR_SDK_INSTALL_DIR)`。实现位于 [extensions.cmake 的 zephyr_get](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/cmake/modules/extensions.cmake#L4081)。本章普通单应用、不使用 snippets 的调用中，它按 **缓存 → 环境 → 当前普通变量** 取第一个已定义值。因此显式 `-D` 能覆盖旧环境，已有缓存也会挡住新 export。

实际实现的完整范围顺序是 `sysbuild_local → sysbuild_global → CACHE → snippets → ENV → current`。sysbuild 是多镜像构建的配置入口；snippets 是命名配置片段。本章未启用二者，所以前面的简化顺序成立。不要把这个顺序扩展成“所有 CMake 变量都这样”。例如 `ZEPHYR_BASE` 由 `ZephyrConfig.cmake` 的独立分支处理，并没有在这里调用同一个函数。

当 `zephyr_get` 从环境取到值时，还会把它写为内部缓存，避免 Ninja 触发重新配置时依赖外部终端恰好保留同一环境。于是会出现以下现象：第一次只 export SDK-A 并配置成功；下一次在同一构建目录 export SDK-B，结果仍使用 A。恢复时为新的工具组合使用新 `-B` 目录，或对允许变更的参数显式重新传 `-D`；不要手工编辑缓存里大量关联项。`BOARD` 还有 `zephyr_check_cache` 的防改板检查，换板尤其应换构建目录。

额外模块是一个必须单独说明的例外。原生 `zephyr_module.cmake` 对 `EXTRA_ZEPHYR_MODULES` 与旧名 `ZEPHYR_EXTRA_MODULES` 使用 **MERGE**，会合并各来源，而不是找到缓存就停止。因此仅写两个空的 `-D` **不能清掉环境里的额外模块**。本章应先在当前 Bash 执行 `unset ZEPHYR_MODULES EXTRA_ZEPHYR_MODULES ZEPHYR_EXTRA_MODULES`，再使用新的构建目录并保留 west 自动发现；空 `-D` 只是清理相应缓存输入。若应用 CMakeLists 自己又定义额外模块，也需检查应用内容。

### 5.5.5\_每个输入由谁约定、在什么时候使用

以下依据均来自 G 盘所核对的原生 Zephyr 修订；文件路径相对于它的源码根。变量名大小写有意义，`Zephyr_DIR` 与 `ZEPHYR_BASE` 不能互换。

| 输入 | 谁约定名称、谁提供值 | 哪一步读取，值应该指向哪里 |
| --- | --- | --- |
| `Zephyr_DIR` | CMake 的 `<PackageName>_DIR` 约定；读者用 `-D` 提供 | 应用 `find_package(Zephyr)` 查 Config 包时，指向含 `ZephyrConfig.cmake` 的 `share/zephyr-package/cmake` |
| `ZEPHYR_BASE` | Zephyr 约定；本例读者指定 | `ZephyrConfig.cmake` 进入 Zephyr 构建逻辑时选择源码根；含 VERSION、boards、cmake，而非应用目录 |
| `ZEPHYR_TOOLCHAIN_VARIANT` | Zephyr 约定；本例指定 `zephyr` | `FindHostTools.cmake` 选择 `cmake/toolchain/zephyr/generic.cmake`；源码默认 GNU 分支，另可明确 `zephyr/gnu` |
| `ZEPHYR_SDK_INSTALL_DIR` | Zephyr/SDK 接口；本例指定 | `FindZephyr-sdk.cmake` 查找 SDK Config 包；本例指向含 `sdk_version`、cmake、gnu 的安装根 |
| `BOARD` | Zephyr 约定；读者选择真实目标 | `boards.cmake` 查 board.yml 并解析限定名，再关联 SoC；原生演示为 `mps2/an386` |
| `ZEPHYR_MODULES` | Zephyr 的显式替换列表；本章不设置 | 非空时替代 west 自动发现，供无 west 等特殊环境使用；不负责下载 |
| `Python3_EXECUTABLE` | CMake FindPython3 接口；读者选解释器 | Zephyr 的 `python.cmake` 优先使用已定义值，并检查最低 Python 3.12；随后形成内部 `PYTHON_EXECUTABLE` |
| `CMAKE_EXPORT_COMPILE_COMMANDS` | CMake 约定；读者设 ON | Ninja 等支持的生成器输出 `compile_commands.json`，用来核对真正编译命令 |

`Zephyr_DIR` 回答“从哪一个包入口进入”，`ZEPHYR_BASE` 回答“以哪棵源码作为基础”。本例将二者指向同一棵源码的对应层次。应用中的 `find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})` 使用环境值作为查找提示；显式包目录与缓存也参与查找，HINTS 不等于强制覆盖所有已选路径。原生 `ZephyrConfig.cmake` 在 CMake 中尚未定义 `ZEPHYR_BASE` 时才从环境取得它，并可依据所加载包的位置推导源码。两项不一致时应纠正输入，不依赖偶然的搜索结果。

SDK 的自动发现是另一件事。不指定安装根时，`FindZephyr-sdk.cmake` 会检查默认位置、CMake 包登记等候选，并检查版本。指定安装根时，当前源码使用 `CONFIG HINTS ... NO_DEFAULT_PATH`，把查找限制到该位置，错误路径会报错。SDK 安装器的 `/c` 登记 SDK，`west zephyr-export` 登记 Zephyr 源码包；二者不是给芯片选型，也不是把工具复制进工程。显式指定两种目录的本例不要求注册。

`SOURCE_ROOT_WIN`、`MODULE_DIRS`、`CMSIS_DIR` 和 `PYTHON_EXE` 是正文自定义的 **Bash 中间变量**，不属于 Zephyr API。只有把它们的值放进上述参数，构建系统才会接收到它们。`TOOLCHAIN_ROOT` 是 Zephyr 工具链接入脚本的根，本例默认源码根；它也不是 SDK 安装根，通常无需读者设置。

### 5.5.6\_按真实执行次序追到编译器

下面是原生 `zephyr_default.cmake`、`dts.cmake`、`kernel.cmake` 串起的主要路径，省略无关检查，但保留“先发现工具、后确定完整硬件配置”的次序：

```text
应用 CMakeLists.txt：find_package(Zephyr ...)
  → ZephyrConfig.cmake：选择源码，加载 zephyr_default.cmake
  → python / zephyr_module：选择 Python，载入外部模块
  → boards：解析 BOARD、板级目录和限定名
  → dts：调用 FindHostTools，先找 SDK 和通用预处理工具
  → Kconfig：结合 board、SoC、prj.conf，形成最终 CONFIG_* 配置
  → arch.cmake：set(ARCH ${CONFIG_ARCH})
  → kernel.cmake → FindTargetTools：加载工具链 target 配置
  → SDK 的 gnu/target.cmake：ARCH=arm → arm-zephyr-eabi
  → GCC target/target_arm：编译器路径、CPU/FPU/ABI 参数
  → CMake 生成 Ninja 规则 → cmake --build 运行编译与链接
```

`FindHostTools.cmake` 里的 SDK 查找发生在完整 Kconfig 处理之前，因此不能简单描述成“先得到全部芯片配置，才第一次找 SDK”。前者先得到可用工具；后者再把目标工具和 CPU 参数落实。

| 派生结果 | 谁产生它 | 是否需要读者 export |
| --- | --- | --- |
| `CONFIG_ARCH`、`CONFIG_CPU_CORTEX_M4` 等 | Kconfig 从板级、SoC 与应用配置计算 | 不需要；查看构建目录 `zephyr/.config` |
| `ARCH` | 原生 `arch.cmake` 从 CONFIG_ARCH 赋值 | 不需要；不是通过 `export ARCH=arm` 代替 BOARD |
| `CROSS_COMPILE_TARGET` | SDK GNU target.cmake 按 ARCH 查映射 | 不需要；本例为 arm-zephyr-eabi |
| `CROSS_COMPILE`、`SYSROOT_DIR` | SDK 根据安装根和目标前缀拼路径 | 不需要；前者是工具前缀，后者指向配套目标头文件/库 |
| `CMAKE_C_COMPILER` | Zephyr GCC 接入脚本查找目标编译器 | 不需要；本例由 SDK 路径派生出 gcc.exe 的完整路径 |
| `SDK_VERSION` 这个 CMake 值 | 已找到的 SDK Config 从其包版本设置 | 不需要；它显示实际找到的 SDK，别与源码根的同名文件混淆 |

最终 `-mcpu=cortex-m4`、`-mthumb` 来自 CPU 配置；是否使用 FPU、哪种浮点调用约定，由该目标最终配置决定。对照 `compile_commands.json` 才能确认实际选了什么。只运行 PATH 上的 `gcc --version`，不能证明这次 Zephyr 构建使用了它。

查源码入口：[原生默认模块顺序](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/cmake/modules/zephyr_default.cmake)、[SDK 查找](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/cmake/modules/FindZephyr-sdk.cmake)、[SDK 目标映射](https://github.com/zephyrproject-rtos/sdk-ng/blob/v1.0.1/cmake/zephyr/gnu/target.cmake)、[ARM GCC 参数](https://github.com/zephyrproject-rtos/zephyr/blob/3777ab91262f93c2c2da7e1ab8cff4e8ea5f4ce4/cmake/compiler/gcc/target_arm.cmake)。这些说明解释当前实验源码的原生构建机制；命令直接调用 CMake。

<a id="section-5-6"></a>

## 5.6\_编译并检查实际使用的版本与目标

**当前步骤：⑤ → ⑥ 编译结果。** 配置成功只说明规则生成成功；执行构建后，应用与内核才变成实际固件。

### 5.6.1\_生成固件并核对工具路径

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；CMake 配置已成功。
cmake --build build-mps2-west
ls -l build-mps2-west/zephyr/zephyr.elf build-mps2-west/zephyr/zephyr.map
```

ELF 是 Executable and Linkable Format，可执行与可链接格式，保存机器码、地址、符号等内容；`.map` 是链接映射，用于观察段与符号的布局。是否另外生成 `.bin` 或 `.hex` 由配置决定，不能只以有没有 bin 判断成功。

先从缓存与最终配置检查选中的对象：

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；只读生成文件。
grep -E '^(BOARD|ZEPHYR_BASE|Zephyr_DIR|ZEPHYR_SDK_INSTALL_DIR|ZEPHYR_TOOLCHAIN_VARIANT|ZEPHYR_MODULES|Python3_EXECUTABLE):' \
  build-mps2-west/CMakeCache.txt
grep -E '^CONFIG_(ARM|CPU_CORTEX_M4|SOC|FPU|FP_HARDABI|FP_SOFTABI)' \
  build-mps2-west/zephyr/.config
cat build-mps2-west/zephyr_modules.txt
```

应看到当前源码、SDK、Python 和树内模块路径，以及 MPS2/Cortex-M4 配置。接着检查 `main.c` 真正使用的编译命令。编译数据库是 JSON 列表，下面的小程序查找文件名以 `/src/main.c` 结尾的一项并打印其命令：

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；已激活 .venv。
python - <<'PY'
import json
from pathlib import Path
entries = json.loads(Path("build-mps2-west/compile_commands.json").read_text(encoding="utf-8"))
for entry in entries:
    if entry["file"].replace("\\", "/").endswith("/src/main.c"):
        print(entry["command"])
PY
```

应看到本次 SDK 内的 `arm-zephyr-eabi-gcc.exe`，以及 `-mcpu=cortex-m4 -mthumb`。若其他板级配置启用浮点支持，还可能看到 `-mfpu` 与 `-mfloat-abi`，分别指定浮点单元和调用约定；应从该构建的最终配置解释，不能把 HC32 参数当作本次 MPS2 的预期输出。

同一 GCC 工具链携带多个目标库变体，按 CPU、指令集和浮点 ABI 选择匹配库。只复制 gcc.exe、混用其他工具链的运行库，可能破坏这一配套关系。

### 5.6.2\_检查生成物确实属于目标架构

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05；用本次 SDK 的工具读取 ELF。
"$(cygpath -u "$ZEPHYR_SDK_INSTALL_DIR")/gnu/arm-zephyr-eabi/bin/arm-zephyr-eabi-readelf.exe" \
  -h build-mps2-west/zephyr/zephyr.elf
```

ELF 头应显示 `ELF32` 与 `Machine: ARM`，这证明输出架构；它本身不能证明是哪一块 ARM 板。结合前面的 BOARD、`.config` 和生成的 `zephyr.dts`，再核对芯片内存与板级身份，布局事实以实验源码的 `boards/arm/mps2/` 和 `soc/arm/mps2/` 为准。

本次只检查原生 MPS2 固件。ELF 的架构和链接布局应与 MPS2 的 `.config`、`zephyr.dts` 对应；它不具备 HC32 的板级身份，不能作为 HC32 固件使用。

这些检查将版本、路径、CPU 参数与固件连接起来。软件构建通过仍不等于实板运行通过，烧录、串口、时钟与外设行为需另行验证。本章不执行硬件操作。

### 5.6.3\_用一个失配反例理解\_SDK\_根目录

复制 5.5.2 的完整配置命令，只改两处：将 `-B build-mps2-west` 换成 `-B build-wrong-sdk`，将 SDK 参数改成 `"-DZEPHYR_SDK_INSTALL_DIR=$ZEPHYR_SDK_INSTALL_DIR/gnu/arm-zephyr-eabi"`。保留其他参数。

预期配置阶段找不到合适的 `Zephyr-sdk` 包。虽然该目录有编译器，它缺少 SDK 根的接入结构。这验证了“能运行 GCC”与“工程正确发现 SDK”并不是同一件事。

恢复时使用正确安装根，回到原来成功的 `build-mps2-west`，或采用新的 `build-mps2-retry` 重新配置。无需删除源码或 SDK。`CMakeCache.txt` 保存之前的路径和选择，所以更换源码、SDK、Python 或 BOARD 时优先使用新构建目录，避免旧缓存干扰判断。

<a id="section-5-7"></a>

## 5.7\_官方\_ZIP、其他芯片和后续开发

**当前步骤：⑥ → ⑦ 迁移与继续开发。** 已经用自建应用走通 SDK 关联。接着在同一份原生源码上编译 hello_world，以区分应用问题与工具环境问题。

### 5.7.1\_给实际解压的官方源码建立连接

2026-10-03 核对的读者解压源码为 **4.5.0-rc1**，其 `SDK_VERSION` 也是 **1.0.1**，CMSIS_6 却要求 `1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8`。目录名字叫 `zephyr-main` 不能代替这些检查。

在一个新的终端使用新的实验目录，避免覆盖前面的 app、模块或构建结果。源码继续保留在读者的原解压位置；输入的是 **直接包含 VERSION 的那一层**：

`pwd` 命令显示当前位置。下面的 `ZIP_SOURCE` 是自定变量，保存统一实验源码路径。先完成定位与建目录；如果新实验目录已存在，检查其内容并另选一个名称，不继续覆盖文件。

变量提示：以下名称均为**教程自定义的临时 Bash 变量，不是 Zephyr 或 CMake 原生接口**。

- `ZIP_SOURCE`：定义见 5.7.1 给实际解压的官方源码建立连接；原生 Zephyr 实验源码根。

```bash
# 当前位置：任意目录；终端：UCRT64，开始独立的上游 ZIP 实验。
ZIP_SOURCE=/g/zephyr_practice/zephyr-main
cat "$ZIP_SOURCE/VERSION"
cat "$ZIP_SOURCE/SDK_VERSION"
mkdir -p "$ZIP_SOURCE/build/learning-tools"
mkdir "$ZIP_SOURCE/build/learning-tools/zephyr-zip-sdk-lab" && cd "$ZIP_SOURCE/build/learning-tools/zephyr-zip-sdk-lab"
```

确认 `pwd` 是新实验目录后，激活 5.4 已创建在源码根的环境：

变量提示：以下名称均为**教程自定义的临时 Bash 变量，不是 Zephyr 或 CMake 原生接口**。

- `ZIP_SOURCE`：定义见 5.7.1 给实际解压的官方源码建立连接；原生 Zephyr 实验源码根。

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/zephyr-zip-sdk-lab；首次创建本实验环境。
source "$ZIP_SOURCE/.venv/Scripts/activate"
python -m pip install -r "$(cygpath -m "$ZIP_SOURCE/scripts/requirements-base.txt")"
python -m pip check
```

复用 5.4.2 与主线 P004 已准备的 west 模块。在本实验目录执行下列查询即可，不需要再下载和重命名另一份 CMSIS：

```bash
# Windows UCRT64；源码根/build/learning-tools/zephyr-zip-sdk-lab；.venv 已激活。
west topdir
west list cmsis_6 -f '{revision} {abspath}'
west forall cmsis_6 -c 'git rev-parse HEAD'
```

复用完整模块，不只复制头文件。SDK 归档与 west 管理的 CMSIS 用途不同。接下来直接使用原生源码自带的 `samples/hello_world`，不依赖其他章节的自建应用：

变量提示：以下名称均为**教程自定义的临时 Bash 变量，不是 Zephyr 或 CMake 原生接口**。

- `SDK_INPUT`：定义见 5.7.1 给实际解压的官方源码建立连接；读者实际的 SDK 解压根。
- `ZIP_SOURCE`：定义见 5.7.1 给实际解压的官方源码建立连接；原生 Zephyr 实验源码根。
- `PYTHON_EXE`：定义见 5.5.1 设置明确的路径；当前已激活 venv 的解释器路径。
- `SDK`：定义见 本篇对应的准备步骤；先确认值已设置；此例实际 SDK 根目录。

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/zephyr-zip-sdk-lab；使用原生 hello_world 应用。
read -r -p '粘贴已安装 SDK 根目录（含 sdk_version，不加引号）：' SDK_INPUT
export ZEPHYR_BASE="$(cygpath -m "$ZIP_SOURCE")"
export ZEPHYR_SDK_INSTALL_DIR="$(cygpath -m "$SDK_INPUT")"
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
unset ZEPHYR_MODULES EXTRA_ZEPHYR_MODULES ZEPHYR_EXTRA_MODULES
PYTHON_EXE="$(python -c 'import sys; print(sys.executable.replace(chr(92), "/"))')"
```

这份上游源码有 `boards/arm/mps2/board.yml` 中的 `mps2/an386`，没有 HC32/UYUP 适配。使用其已有 Cortex-M4 目标，检验同一个 ARM SDK 与另一份解压源码能否配合：

变量提示：以下名称均为**教程自定义的临时 Bash 变量，不是 Zephyr 或 CMake 原生接口**。

- `PYTHON_EXE`：定义见 5.5.1 设置明确的路径；当前已激活 venv 的解释器路径。

```bash
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/zephyr-zip-sdk-lab；为上游已有目标使用新的构建目录。
cmake -S "$ZEPHYR_BASE/samples/hello_world" -B build-mps2-west -G Ninja \
  -DBOARD=mps2/an386 \
  "-DZephyr_DIR=$ZEPHYR_BASE/share/zephyr-package/cmake" \
  "-DZEPHYR_BASE=$ZEPHYR_BASE" \
  "-DZEPHYR_SDK_INSTALL_DIR=$ZEPHYR_SDK_INSTALL_DIR" \
  -DZEPHYR_TOOLCHAIN_VARIANT=zephyr \
  -DEXTRA_ZEPHYR_MODULES= -DZEPHYR_EXTRA_MODULES= \
  "-DPython3_EXECUTABLE=$PYTHON_EXE" \
  -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build build-mps2-west
```

将 5.6 节缓存、编译数据库和 ELF 头的检查路径改为 `build-mps2-west`，应看到上游源码路径、刚下载的 CMSIS_6、同一个 ARM GCC 和 Cortex-M4 参数。不要对这个目标运行 HC32 专用镜像检查，也不要将生成的固件烧到 HC32 上。本节只编译，QEMU 模拟器不是完成这一编译的前提。

### 5.7.2\_真正换成另一颗芯片时改变哪些内容

SDK 下载成功不会给上游 ZIP 自动添加 HC32 支持。若要在这份新上游源码上开发 HC32，需要移植并验证 board、SoC、设备树、GPIO/串口驱动、模块与配置入口的兼容性；只复制 HAL 或填写一个 BOARD 名称都不够。已有移植材料可用于对照，但每项修改仍须在实验源码中核对和验证。

换芯片按以下顺序重新判断：

| 发生的变化 | 必须重新确认 | 不必自动重做的事情 |
| --- | --- | --- |
| HC32 换另一个 Cortex-M4 MCU | board/SoC、模块、内存、时钟、引脚、驱动和最终配置 | 不必仅因芯片型号不同就换 ARM GCC |
| ARM 换 RISC-V 等架构 | 该源码实际支持的目标及 SDK 中对应工具链 | SDK 发布版本仍先由源码兼容要求决定 |
| Zephyr 源码升级 | SDK_VERSION、兼容要求、模块 revision、移植接口 | 不能仅由芯片不变推断所有依赖不变 |
| 只改应用 C 代码 | 对应 app 和构建输出 | 通常不需要重新下载 SDK 和源码 |

板级描述必须符合真实芯片封装和 PCB 连接。将来在实验源码中移植 HC32 时，需核对实装晶振、Flash/SRAM、引脚与驱动；工具链版本检查不能代替这些检查。

### 5.7.3\_下次开发与常见失败的恢复

路径未改变时，构建目录已经缓存源码、SDK 和 Python 位置。下次打开 UCRT64，激活对应环境后可继续编译：

```bash
# 当前位置：任意目录；继续前面已成功配置的 HC32 实验。
cd "$HOME/zephyr-download-lab"
# 当前位置：/g/zephyr_practice/zephyr-main/build/learning-tools/sdk-p05。
source .venv/Scripts/activate
cmake --build build-mps2-west
```

需要重新配置时，重新执行本章的路径设置和完整 CMake 命令。可以把自己的路径与配置命令保存在本机脚本中；含绝对路径的本机设置不作为可移植项目配置提交。源码、SDK 或虚拟环境搬家后，用正确路径创建新构建目录，虚拟环境按依赖清单重建。

后续继续在 `G:\zephyr_practice\zephyr-main` 开发。每次构建都明确源码、模块、SDK、应用和目标；切换输入时使用新的构建目录，保留旧结果用于对照。

| 现象 | 优先检查 | 恢复方法 |
| --- | --- | --- |
| Release 下载 404 或连接失败 | 版本、附件名、浏览器/curl 代理 | 回到同版官方发布页核对链接，不猜文件名 |
| 摘要不一致 | 文件截断或混入不同发布版附件 | 重新取得失败文件并校验 |
| setup 又下载工具链 | gnu/arm-zephyr-eabi 是否正确解压 | 修正层次后再安装，不把压缩包当已安装目录 |
| gcc 不能在 Windows 执行 | 是否下载了 Linux 或其他主机包 | 使用 Windows x86-64 附件并完整解压 |
| CMake 找不到 Zephyr | Zephyr_DIR、ZEPHYR_BASE 是否指向正确源码 | 修正路径，使用新构建目录 |
| 找不到合适的 Zephyr-sdk | SDK 根、sdk_version、兼容要求 | 指向含版本与 CMake 接入文件的根 |
| 未知 BOARD | 当前源码是否真的包含板级与 SoC 支持 | 选择已有目标，或完成正式移植 |
| CMSIS 头文件缺失 | 模块版本、解压层次、module.yml、模块列表 | 取当前源码清单版本并显式传入根目录 |
| 仍使用旧 SDK | CMakeCache.txt 保存的路径 | 新建构建目录并重新配置 |
| 编译成功但板上不运行 | 板级配置、链接布局、时钟和驱动 | 进入实板调试，不能靠重新下载 SDK 代替定位 |

现在可以从仓库版本找到 SDK，从 SDK 发布找到 GCC，从芯片配置找到目标工具链，再从实际编译数据库和 ELF 反向核对。主机工具的完整维护和离线安装继续见 P006；本章的[验证记录](VALIDATION.md)区分了实际完成的编译与未执行的新机安装、烧录步骤。

[参考资料目录](README.md) · [上一篇](P004_如何从west.yml获得需要下载的包.md) · [下一篇](P006_环境依赖需要安装的工具.md)
