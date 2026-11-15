---
id: learning.zephyr-docs.west.west_extra
title: 其他Zephyr扩展命令
kind: reference
status: maintained
domains: [zephyr, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/west/zephyr-cmds.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第8章\_其他Zephyr扩展命令

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/west/zephyr-cmds.html)。本次读取日期：2026-10-14；基线为所保存的 `latest` 页面，HTML摘要见[来源记录](../SOURCES.md)。

本页介绍多种 **Zephyr扩展命令（Zephyr Extension Commands）**。基本机制见[west基本概念](P002_基本概念.md)。

## 8.1\_列出开发板：west boards

`boards` 命令直接列出 Zephyr 支持的开发板，不必另查其他信息源：

```shell
west boards
```

默认使用预设格式列出全部受支持开发板。通过 `--format`（或 `-f`）可自定显示格式：

```shell
west boards -f "{arch}:{name}"
```

格式选项的更多说明见：

```shell
west boards -h
```

## 8.2\_命令行补全脚本：west completion

`completion` 输出 **shell补全（Shell Completion）**脚本，可直接用于启用受支持终端的补全功能。目前支持 Bash、Zsh、Fish，以及 PowerShell；PowerShell 仅支持开发板限定符补全。

更多使用说明见命令帮助：

```shell
west help completion
```

## 8.3\_安装CMake包：west zephyr-export

此命令把当前 Zephyr 安装登记为 **CMake配置包（CMake Config Package）**，写入当前用户的 **CMake包注册表（CMake User Package Registry）**。

Windows 中，该注册信息位于 `HKEY_CURRENT_USER\Software\Kitware\CMake\Packages`；Linux 和 macOS 中位于 `~/.cmake/packages`。它们分别是当前用户注册表键和主目录下的标准位置，并非作者机器的固定目录。

可在建立 Zephyr 工作区时执行该命令。之后，工作区外应用的 `CMakeLists.txt` 也可以通过以下方式找到 Zephyr 仓库：

```cmake
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
```

实现细节见官方源码 [share/zephyr-package/cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/zephyr-package/cmake)，完整用法见[Zephyr CMake包](../build_system/P002_Zephyr_CMake包.md)。

<a id="west-spdx"></a>

## 8.4\_软件物料清单：west spdx

该命令将一次 Zephyr 构建的 **软件物料清单（Software Bill of Materials，SBOM）**生成为一组 [SPDX](https://spdx.dev/) 文档，记录参与构建的源文件、产生的构建产物及其关系，并扫描每个文件的许可证、版权和哈希值。

### 8.4.1\_选择SPDX版本

`west spdx` 支持 SPDX 的两大规范系列，默认版本为 2.3，其他版本用 `--spdx-version` 选择。SPDX 2.3 是 2.2 的超集，增加了 `PrimaryPackagePurpose` 等字段。需要兼容尚不理解 SPDX 3 的工具时选择 SPDX 2.x；需要下面介绍的更丰富、机器可读的构建来源信息时，选择 SPDX 3.0 或更新版本。

**原文注意：**SPDX 3.1 支持是实验性的，因为该规范仍在开发。

### 8.4.2\_生成SPDX文档

1. 在项目中启用 `CONFIG_BUILD_OUTPUT_META`，使构建记录 `west spdx` 所需信息。
2. 构建应用：

```shell
west build -d BUILD_DIR [...]
```

3. 基于该构建目录生成文档：

```shell
west spdx -d BUILD_DIR
```

默认生成 SPDX 2.3 的**标签—值（Tag-Value）**格式文档。使用 `--spdx-version` 可改为 2.2 或 3.0，例如：

```shell
west spdx -d BUILD_DIR --spdx-version 3.0
```

**原文注意：**使用[系统构建](../sysbuild/P001_系统构建.md)时，应指定要生成 SBOM 的实际应用，而不是仅指定顶层构建目录。例如应用名为 `hello_world`：

```shell
west build --sysbuild -d BUILD_DIR
west spdx -d BUILD_DIR/hello_world
```

> 译注：`BUILD_DIR` 与 `[...]` 是示例占位，需选择实际构建目录并提供应用、目标板等构建所需参数；方括号省略标记不直接输入。以下输出是工具行为说明，本次没有执行安装、构建或生成操作。

### 8.4.3\_输出文档

默认输出到 `BUILD_DIR/spdx/`，可以用 `-s` 改变位置。不同 SPDX 版本产生相同的一组 **物料清单（Bill of Materials，BOM）**文档，扩展名不同：SPDX 2.x 的标签—值格式使用 `.spdx`，SPDX 3.0 的 **JSON关联数据（JSON for Linked Data，JSON-LD）**格式使用 `.jsonld`。

| 文档名 | 内容 |
| --- | --- |
| `app` | 用于构建的应用源文件 |
| `zephyr` | 本次构建实际使用的 Zephyr 源文件 |
| `build` | 构建输出文件 |
| `modules-deps` | 模块依赖，详见[模块与外部项目](../modules/P001_模块与外部项目.md) |

对于 SPDX 3.0，每份文档都声明符合 Core、Software 和 Simple Licensing **配置集（Profile）**；`build.jsonld` 还声明符合 Build 配置集，用于记录产物怎样生成。

对清单中的每个文件进行扫描，记录 SHA512、SHA256、SHA1 哈希，以及许可证和版权。后两项由 REUSE 项目的第三方 `reuse` 工具解析，因此 `west spdx` 支持 [REUSE规范](https://reuse.software/spec/)规定的全部声明方式：文件内 `SPDX-License-Identifier` 和 `SPDX-FileCopyrightText` 注释、文件旁的 `.license` 文件，以及仓库根目录 `REUSE.toml` 中对整组路径的注记。原文称最后一种形式是为无法在自身保存注释的文件（尤其是二进制块）声明许可证的唯一方式。

> 译注：原文“唯一方式”的表述与同段列出的外置 `.license` 方式存在需要核对的范围差异；这里保留其原意，不据此排除 REUSE 规范允许的其他外置声明方式。具体支持情况以所用 REUSE 版本及该规范为准。

找到的信息在 SPDX 2.x 中写入 `LicenseInfoInFile`、`LicenseConcluded`、`FileCopyrightText`，在 SPDX 3.0 中写入对应元素的许可证与版权属性。

**原文注意：**版权提取采用**启发式方法（Heuristics）**，可能无法提取完整声明，所以 `FileCopyrightText` 尽力提供结果；这一做法符合 SPDX 规范建议。

### 8.4.4\_关系

SPDX 关系描述 CMake 构建目标之间的依赖、互相链接的目标，以及编译生成库文件的源文件。两大规范系列对 **构建来源（Build Provenance）**的表示不同：

- SPDX 2.x 为每个产物记录文件级 `GENERATED_FROM` 关系，指向生成该产物的源文件；启用 `--analyze-includes` 时也包括头文件。
- SPDX 3.0 使用 Build 配置集，以构建生命周期范围内的 `hasInput`、`hasOutput`、`usesTool` 关系表达来源。

### 8.4.5\_构建配置集：SPDX 3.0

生成 SPDX 3.0 时，`west spdx` 填充 [Build配置集](https://spdx.github.io/spdx-spec/v3.0.1/model/Build/Build/)，让 SBOM 同时记录构建内容和构建方法。信息自动取自 **CMake文件API（CMake File API）**，存入 `build.jsonld`。

`build_Build` 元素描述整个构建，包括构建类型、CMake 生成器与构建配置，以及 `BOARD`、`ARCH` 等选定环境变量。工具链中的 CMake、编译器、汇编器、链接器和归档器分别记录为 `Tool` 元素，各自含路径和版本。构建范围内的关系将构建与输入（源码包和已编译文件）、输出（最终镜像）以及使用的工具连接起来。

静态库等每个中间目标也有自己的子构建，记录生成该产物的准确源文件、工具和编译标志，因此能够追溯任意输出的生成方式。

### 8.4.6\_命令行选项

| 选项 | 含义 |
| --- | --- |
| `-i`、`--init` | 在配置构建目录前创建 CMake 文件API查询。已弃用，计划在 Zephyr 5.0 移除；启用 `CONFIG_BUILD_OUTPUT_META` 的构建现在会自行请求该查询。 |
| `-n PREFIX` | 设置输出 SPDX 文档的命名空间前缀，见[SPDX文档创建信息](https://spdx.github.io/spdx-spec/v2.2.2/document-creation-information/)。省略时，按默认格式使用随机的通用唯一标识符（Universally Unique Identifier，UUID）生成命名空间。原文分别引用规范第6条和第2.5节。 |
| `-s SPDX_DIR` | 指定输出目录，替代 `BUILD_DIR/spdx/`。 |
| `--spdx-version {2.2,2.3,3.0,3.1}` | 选择规范版本，默认2.3。 |
| `--analyze-includes` | 除 `.c`、`.S` 等已编译源文件外，尝试识别每个 `.c` 文件实际包含的头文件。它按真实构建参数为每个C文件调用编译器作一次试运行（Dry Run），因此更耗时。 |
| `--include-sdk` | 与 `--analyze-includes` 配合，另外生成 `sdk.spdx` 或 `sdk.jsonld`，记录来自SDK的头文件。原文称其为“第四份”文档。 |

> 译注：上文基础输出列表已包含四项；因此“第四份”是原文残留表述，不能据此推断包含 SDK 后仍只有四份输出。实际文件集合以所用工具版本和选项为准。

**原文警告：**目前不支持为 `native_sim` 平台生成 SBOM。

<a id="west-blobs"></a>

## 8.5\_处理二进制块：west blobs

`blobs` 用于操作模块 `module.yml` 中声明的**二进制块（Binary Blob）**，提供列出、获取和清理（删除）三个子命令。模块声明方式见[模块与外部项目](../modules/P001_模块与外部项目.md)，背景见[官方二进制块说明](../contributing/P008_二进制文件.md#bin-blobs)。

列出二进制块并指定输出格式：

```shell
west blobs list -f '{module}: {type} {path}'
```

`-f/--format` 可用变量的完整列表见 `west blobs -h`。获取方式类似：

```shell
west blobs fetch
```

下载的文件存放在对应模块仓库根目录下的 `zephyr/blobs/`。删除它们使用：

```shell
west blobs clean
```

可以将模块名作为命令行参数，只对指定模块执行列出、获取或清理。`west blobs fetch` 还可用 `--allow-regex` 按正则表达式限制下载对象，例如仅下载 ESP32 变体：

```shell
# For example, only download esp32 blobs, skip the other variants
west blobs fetch hal_espressif --allow-regex 'lib/esp32/.*'
```

`--auto-cache` 命令行选项或 `blobs.auto-cache` 配置项指定自动缓存目录。启用后，缺失的二进制块下载成功时会自动加入缓存。`--cache-dirs` 或 `blobs.cache-dirs` 可指定更多缓存目录，多个目录用分号分隔。

`west blobs fetch` 会搜索全部已配置缓存，包括自动缓存。缓存文件可以保留原文件名，也可以使用 `<filename>.<sha>` 形式的 SHA-256 后缀。找到后从缓存复制到目标位置；没有找到则从配置的 URL 下载。

`blobs.mirrors` 支持配置一个或多个下载镜像。值是 JSON 对象：每个键为远端 URL 前缀，每个值为单个镜像 URL 前缀字符串，或多个前缀组成的字符串数组。

一个远端前缀对应单个镜像：

```shell
west config blobs.mirrors '{"https://github.com/": "https://example.com/github-mirror/"}'
```

同一前缀对应多个镜像，按数组顺序尝试：

```shell
west config blobs.mirrors '{
  "https://github.com/": [
    "https://example.com/github1-mirror/",
    "https://example.com/github2-mirror/"
  ]
}'
```

对每个二进制块 URL，工具尝试所有前缀匹配的镜像；像 Git 的 `insteadOf` 一样，先尝试最长、最具体的匹配前缀，再尝试更短的前缀。同一远端前缀下按配置顺序尝试镜像，全部失败后才回退到原始 URL。

## 8.6\_Twister包装命令：west twister

这是 [Twister测试运行器](../twister/P001_Twister测试运行器.md)的包装命令，可通过 west 调用：

```shell
west twister -help
west twister -T tests/ztest/base
```

<a id="west-bindesc"></a>

## 8.7\_读取二进制描述符：west bindesc

`bindesc` 读取可执行文件的**二进制描述符（Binary Descriptor）**，目前支持 `.bin`、`.hex`、`.elf` 和 `.uf2` 输入。更多概念见[官方二进制描述符译文](../data_utilities/P010_二进制描述符.md#binary-descriptors)。

搜索镜像中特定描述符：

```shell
west bindesc search KERNEL_VERSION_STRING build/zephyr/zephyr.bin
```

按类型和标识符搜索自定义描述符：

```shell
west bindesc custom_search STR 0x200 build/zephyr/zephyr.bin
```

转储全部描述符：

```shell
west bindesc dump build/zephyr/zephyr.bin
```

将描述符数据区域提取到文件：

```shell
west bindesc extract
```

列出已知的标准描述符名称：

```shell
west bindesc list
```

打印描述符在镜像内的偏移：

```shell
west bindesc get_offset
```

> 译注：原页最后三条命令按原样保留；所用版本需要的输入文件、输出文件等参数应通过对应子命令的 `-h` 查明，不把没有参数的示意自动当作完整提取操作。

## 8.8\_使用GNU Global索引源码：west gtags

**原文强调：**必须先安装 [GNU Global](https://www.gnu.org/software/global/)提供的 `gtags` 和 `global` 程序。

以下命令为整个 west 工作区建立标签文件：

```shell
west gtags
```

它在工作区顶层目录建立 `GTAGS`，并在同一位置建立 `GPATH` 和 `GRTAGS` 等 Global 元数据文件。随后可在工作区内任何位置运行 `global`，通过标签文件查找符号定义。

例如，从 `zephyr/drivers` 目录查找 `arch_system_halt()` 的所有定义：

```console
$ cd zephyr/drivers
$ global -x arch_system_halt
arch_system_halt   65 ../arch/arc/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt  455 ../arch/arm64/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt  137 ../arch/nios2/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt   18 ../arch/posix/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt   17 ../arch/x86/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt  126 ../arch/xtensa/core/fatal.c FUNC_NORETURN void arch_system_halt(unsigned int reason)
arch_system_halt   21 ../kernel/fatal.c FUNC_NORETURN __weak void arch_system_halt(unsigned int reason)
```

输出依次显示符号名、定义行号、文件相对路径和该行内容，覆盖全部定义位置。这也适合查找厂商**硬件抽象层（Hardware Abstraction Layer，HAL）**函数；工具更多用法见 `global` 的手册页。

应调用 `global`，不是 `west global`。`global` 已会从当前工作目录开始搜索 `GTAGS`，无需额外的 west 包装命令；这也是必须在工作区内运行的原因。

> 译注：示例中的 `$` 是终端提示符；函数位置和行号是原文示例输出，不是当前源码检索结果。

## 8.9\_管理补丁：west patch

`patch` 以受控方式向 Zephyr 或其模块应用补丁，方便采用 [T2星形拓扑](P004_工作区.md)的外部应用自动化处理并跟踪状态。`patches.yml` 保存补丁元数据，用于衔接官方发行版之间尚未进入版本的修改；使用者可以查看上游合入进展，决定升级下个发行版前移除哪些补丁。

| 子命令 | 作用 |
| --- | --- |
| `apply` | 应用 `patches.yml` 中列出的补丁。 |
| `reverse` | 逆向撤销清单中已应用的补丁。 |
| `clean` | 清理全部已应用补丁，将仓库重置到清单检出状态。 |
| `list` | 列出清单中的全部补丁。 |
| `gh-fetch` | 从 GitHub 拉取请求（Pull Request，PR）取得补丁。 |

示例目录：

```text
west-workspace/
└── application/
   ...
   ├── west.yml
   └── zephyr
       ├── module.yml
       ├── patches
       │   ├── bootloader
       │   │   └── mcuboot
       │   │       └── my-tweak-for-mcuboot.patch
       │   └── zephyr
       │       └── my-zephyr-change.patch
       └── patches.yml
```

该例的 `west.yml` 固定一个 Zephyr 修订，例如 `v4.1.0`，并针对该修订及应用使用的其他模块修订应用补丁。应用需要两项修改，一项针对 Zephyr，另一项针对 MCUboot：

```yaml
patches:
  - path: zephyr/my-zephyr-change.patch
    sha256sum: c676cd376a4d19dc95ac4e44e179c253853d422b758688a583bb55c3c9137035
    module: zephyr
    author: Obi-Wan Kenobi
    email: obiwan@jedi.org
    date: 2025-05-04
    upstreamable: false
    comments: |
      An application-specific change we need for Zephyr.
  - path: bootloader/mcuboot/my-tweak-for-mcuboot.patch
    sha256sum: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    module: mcuboot
    author: Darth Sidious
    email: sidious@sith.org
    date: 2025-05-04
    merge-pr: https://github.com/zephyrproject-rtos/zephyr/pull/<pr-number>
    issue: https://github.com/zephyrproject-rtos/zephyr/issues/<issue-number>
    merge-status: true
    merge-commit: 1234567890abcdef1234567890abcdef12345678
    merge-date: 2025-05-06
    apply-command: git apply
    comments: |
      A change to mcuboot that has been merged already. We can remove this
      patch when we are ready to upgrade to the next Zephyr release.
```

> 译注：两段 `comments` 分别说明“应用专用的 Zephyr 修改”和“已经在上游合入、升级到下个 Zephyr 版本时可移除的 MCUboot 修改”。人员、邮箱、提交号、哈希及 PR 链接是官方示例数据，不代表本次提交或有效的补丁文件。

可自动应用这些补丁，例如：

```shell
west init -m <manifest repo> <workspace>
cd <workspace>
west update
west patch apply
```

准备升级 Zephyr 时，将 `west.yml` 改为下个发行版，例如 `v4.2.0`；从 `patches.yml` 及外部应用仓库中移除不再需要的补丁，如示例中的 `my-tweak-for-mcuboot.patch`，然后执行：

```shell
west patch clean
west update
west patch apply --roll-back # roll-back all patches if one does not apply cleanly
```

也可以逆向撤销补丁，而不清理全部模块。这样保留无冲突、与补丁无关的修改，只移除补丁引入的变化，适合在应用中开发和测试补丁时保留模块的手工编辑：

```shell
west patch reverse
```

修改补丁后，记得在 `patches.yml` 更新 SHA-256 校验值：

```console
sha256sum zephyr/patches/zephyr/my-zephyr-change.patch
7d57ca78d5214f422172cc47fed9d0faa6d97a0796c02485bff0bf29455765e9
```

`west patch gh-fetch` 还可从 GitHub PR 下载补丁，并自动创建或更新 `patches.yml`。已经有多个上游 PR 时，这种方式尤其方便：

```shell
west patch gh-fetch --owner zephyrproject-rtos --repo zephyr --pull-request <pr-number> \
  --module zephyr --split-commits
```

上述命令会建立以下结构，为该 PR 的每个提交分别生成补丁：

```text
zephyr
├── patches
│   ├── first-commit-from-pr.patch
│   ├── second-commit-from-pr.patch
│   └── third-commit-from-pr.patch
└── patches.yml
```

> 译注：`<manifest repo>`、`<workspace>`、`<pr-number>` 都需要替换。`clean` 会重置仓库；需要保留无关手工修改时应理解 `reverse` 与 `clean` 的区别。`--roll-back` 表示有补丁不能干净应用时回滚本轮补丁。这里仅翻译操作步骤，本次没有初始化、更新、清理或修改任何模块。

## 8.10\_管理Zephyr SDK：west sdk

`west sdk` 是 Zephyr 专用的 west 命令，用于列出和安装 **Zephyr软件开发工具包（Zephyr Software Development Kit，Zephyr SDK）**及其工具链。

### 8.10.1\_列出SDK与工具链

```shell
west sdk list
```

该命令显示已安装的 SDK 版本、可用的 SDK 发行版，以及每个 SDK 包含的工具链。

### 8.10.2\_安装SDK

```shell
west sdk install
```

命令可能进入交互模式，提示选择 SDK 或工具链。用 `--toolchains` 明确指定工具链时，采用非交互方式，官方建议自动化场景使用这种方式。例如只安装指定的工具链：

```shell
west sdk install --toolchains arm-zephyr-eabi riscv64-zephyr-elf
```

若不确定需要哪些工具链，先运行 `west sdk list` 查看可选项，避免下载不需要的工具链，从而节省数 GB 磁盘空间和下载时间。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：使用 west 构建、烧录与调试](P007_构建烧录与调试.md) · [本模块主线目录](../reading/west.md) · [全部主线](../reading/README.md) · [下一篇：二进制镜像签名](P009_二进制镜像签名.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：构建烧录与调试](P007_构建烧录与调试.md) · [下一章：二进制镜像签名](P009_二进制镜像签名.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
