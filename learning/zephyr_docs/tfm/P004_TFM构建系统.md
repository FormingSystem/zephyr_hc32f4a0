---
id: learning.zephyr-docs.tfm.page-4
title: TFM构建系统
kind: reference
status: maintained
domains: [zephyr, tfm, security]
source_url: https://docs.zephyrproject.org/latest/services/tfm/build.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_TFM构建系统

原文：[官方页面](https://docs.zephyrproject.org/latest/services/tfm/build.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 4.1\_构建流程

构建有效的 `_ns` 板级目标时，系统会在后台构建 TF-M，并与 Zephyr 非安全应用集成。大多数情况下无需了解 TF-M 构建系统的内部细节；以下命令即可构建一对 TF-M 与 Zephyr 镜像，并在 QEMU 中运行，无需额外步骤。

```sh
$ west build -p auto -b mps2/an521/cpu0/ns samples/tfm_integration/psa_protected_storage/ -t run
```

译注：`_ns` 是原页用语，命令采用当前层级形式的 `mps2/an521/cpu0/ns`。本节以主机工具、目标工具链、west 模块及[TF-M 依赖](P003_TFM环境与硬件要求.md)已经准备好为前提；命令从 Zephyr 源码根目录执行。生成镜像不等于已经在实板上验证。

部署之前，需要理解和使用构建输出，并为安全镜像（Secure Image）与非安全镜像（Non-Secure Image）签名，因此下面进一步说明产物及关键步骤。

## 4.2\_TF-M 构建生成的镜像（Images Created by the TF-M Build）

TF-M 构建系统生成以下可执行文件：

- `tfm_s`：TF-M 安全固件。
- `tfm_ns`：TF-M 非安全应用，仅用于回归测试（Regression Tests）。
- `bl2`：启用后生成的 TF-M MCUboot 引导加载程序。

每一项都生成 `.bin`、`.hex`、`.elf` 和 `.axf` 文件。

构建系统还生成 `tfm_s`、`tfm_ns` 的已签名版本，以及合并两者的文件：

- `tfm_s_signed`。
- `tfm_ns_signed`。
- `tfm_s_ns_signed`。

这些签名产物只生成 `.bin` 文件。

除运行 TF-M 回归测试套件外，TF-M 自带的非安全应用会被舍弃，改用 Zephyr 非安全应用。Zephyr 构建系统通常自行对 `tfm_s` 和 Zephyr 非安全应用签名，详见下文。

`tfm` 目标（Target）通过属性（Property）保存上述路径。例如，下列表达式解析为 `<path>/tfm_s.hex`：

```cmake
$<TARGET_PROPERTY:tfm,TFM_S_HEX_FILE>
```

各属性的完整定义可查看 `tfm` 模块顶层 `CMakeLists.txt`。

## 4.3\_镜像签名（Signing Images）

当 [`CONFIG_TFM_BL2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_BL2) 为 `y` 时，TF-M 使用安全引导加载程序 BL2，固件镜像必须用私钥（Private Key）签名。更新过程中，引导加载程序使用对应公钥（Public Key）验证固件；公钥保存在安全引导加载程序的固件镜像内。

原文默认使用 `<tfm-dir>/bl2/ext/mcuboot/root-rsa-3072.pem` 签名安全镜像，使用 `<tfm-dir>/bl2/ext/mcuboot/root-rsa-3072_1.pem` 签名非安全镜像。可以且应当通过 [`CONFIG_TFM_KEY_FILE_S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_KEY_FILE_S) 和 [`CONFIG_TFM_KEY_FILE_NS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_KEY_FILE_NS) 覆盖这些默认 `.pem` 密钥。

原文强调：为了满足 [PSA 一级认证（PSA Certified Level 1）](https://www.psacertified.org/security-certification/psa-certified-level-1/)要求，**必须用新密钥对替换默认 `.pem` 文件**。

生成新的公私钥对可使用以下命令：

```sh
$ imgtool keygen -k root-rsa-3072_s.pem -t rsa-3072
$ imgtool keygen -k root-rsa-3072_ns.pem -t rsa-3072
```

随后可将新 `.pem` 文件放到其他位置，例如 Zephyr 应用文件夹，并在 `prj.conf` 中通过 [`CONFIG_TFM_KEY_FILE_S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_KEY_FILE_S) 和 [`CONFIG_TFM_KEY_FILE_NS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_KEY_FILE_NS) 引用。

> 原文警告：务必将私钥文件保存在安全可靠的位置。若丢失该密钥，将无法为后续固件镜像签名，现场设备也将无法继续更新。

译注：这里保留原文 RSA-3072 示例。当前官方 `Kconfig.tfm` 的默认密钥文件名由 `CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE` 组成，并非所有配置都固定采用 RSA-3072；应同时核对所选签名算法与实际密钥。`<tfm-dir>` 表示当前工作区中的 TF-M 模块根目录，不是某台机器的固定路径。

内置签名脚本运行后，会创建 `tfm_merged.hex` 和 `tfm_merged.bin`，其中包含 `bl2`、`tfm_s` 与 Zephyr 应用三个二进制部分。这些文件可烧录到开发板，或在 QEMU 中运行。

## 4.4\_输出文件（Output Files）

Zephyr TF-M 构建完成后，存在以下输出：

| 文件名（Filename） | 来源（Created From） | 引导加载程序标志（Bootloader Flags） | 用途（Usage） |
| --- | --- | --- | --- |
| `tfm_s_signed.{hex/bin}` | TF-M 安全镜像 | 已签名（Signed） | `CONFIG_TFM_MCUBOOT_IMAGE_NUMBER == 2` 时用于空中升级（Over-the-Air，OTA） |
| `zephyr_ns_signed.{hex/bin}` | Zephyr 非安全镜像 | 已签名（Signed） | `CONFIG_TFM_MCUBOOT_IMAGE_NUMBER == 2` 时用于 OTA 升级 |
| `tfm_s_zephyr_ns_signed.{hex/bin}` | TF-M 安全镜像和 Zephyr 非安全镜像 | 已签名（Signed） | `CONFIG_TFM_MCUBOOT_IMAGE_NUMBER == 1` 时用于 OTA 升级 |
| `tfm_merged.{hex/bin}` | 引导加载程序、TF-M 安全镜像和 Zephyr 非安全镜像 | 已签名、已确认（Signed, Confirmed） | 生产烧录（Production Programming），由 `west flash` 烧录 |

## 4.5\_自定义 CMake 参数（Custom CMake Arguments）

将 Zephyr 应用与 TF-M 一起构建时，可能需要控制传入 TF-M 构建过程的 CMake 参数。Zephyr 提供若干 Kconfig 选项控制 TF-M 构建，但并未覆盖 TF-M 构建系统支持的每个 CMake 参数。

可通过 `zephyr_property_target` 上的 `TFM_CMAKE_OPTIONS` 属性传递自定义参数。例如，将以下片段写入应用的 `CMakeLists.txt`，即可传入 `-DFOO=bar`。

```cmake
set_property(TARGET zephyr_property_target
             APPEND PROPERTY TFM_CMAKE_OPTIONS
             -DFOO=bar
)
```

注意：`TFM_CMAKE_OPTIONS` 是列表（List），可以追加多个选项；也支持 CMake 生成器表达式（Generator Expression），如 `$<1:-DFOO=bar>`。

由于该属性是列表参数，传递给 TF-M 构建系统之前会先展开。因此，选项自身若包含列表参数，必须适当转义，避免被提前拆开。

```cmake
set_property(TARGET zephyr_property_target
             APPEND PROPERTY TFM_CMAKE_OPTIONS
             -DFOO="bar\\\;baz"
)
```

## 4.6\_占用空间与内存使用（Footprint and Memory Usage）

构建系统提供目标来查看和分析生成镜像中的 RAM 与 ROM 使用情况。这些工具针对最终镜像工作，报告 RAM、ROM 中使用的符号与代码大小。更多信息见 [占用空间与内存使用](../optimizations/P003_优化分析工具.md#footprint-tools)。

以下各组命令从 Zephyr 源码根目录执行。原代码注释依次表示“从 Zephyr 仓库根目录执行”“使用 CMake 配置基于 Ninja 的构建系统”“在生成的构建系统上运行构建工具”。west 与 CMake／Ninja 是两种调用方式。

### 4.6.1\_TF-M 安全固件的 RAM 报告

使用 `tfm_ram_report` 获取 TF-M 安全固件 `tfm_s` 的 RAM 报告。

使用 west：

```sh
# From the root of the zephyr repository
west build -b mps2/an521/cpu0/ns samples/hello_world
west build -t tfm_ram_report
```

使用 CMake 与 Ninja：

```sh
# From the root of the zephyr repository
# Use cmake to configure a Ninja-based buildsystem:
cmake -Bbuild -GNinja -DBOARD=mps2/an521/cpu0/ns samples/hello_world

# Now run the build tool on the generated build system:
ninja -Cbuild tfm_ram_report
```

### 4.6.2\_TF-M 安全固件的 ROM 报告

使用 `tfm_rom_report` 获取 `tfm_s` 的 ROM 报告。

使用 west：

```sh
# From the root of the zephyr repository
west build -b mps2/an521/cpu0/ns samples/hello_world
west build -t tfm_rom_report
```

使用 CMake 与 Ninja：

```sh
# From the root of the zephyr repository
# Use cmake to configure a Ninja-based buildsystem:
cmake -Bbuild -GNinja -DBOARD=mps2/an521/cpu0/ns samples/hello_world

# Now run the build tool on the generated build system:
ninja -Cbuild tfm_rom_report
```

### 4.6.3\_TF-M MCUboot 的 RAM 报告

启用 TF-M MCUboot 后，使用 `bl2_ram_report` 获取其 RAM 报告。

使用 west：

```sh
# From the root of the zephyr repository
west build -b mps2/an521/cpu0/ns samples/hello_world
west build -t bl2_ram_report
```

使用 CMake 与 Ninja：

```sh
# From the root of the zephyr repository
# Use cmake to configure a Ninja-based buildsystem:
cmake -Bbuild -GNinja -DBOARD=mps2/an521/cpu0/ns samples/hello_world

# Now run the build tool on the generated build system:
ninja -Cbuild bl2_ram_report
```

### 4.6.4\_TF-M MCUboot 的 ROM 报告

启用 TF-M MCUboot 后，使用 `bl2_rom_report` 获取其 ROM 报告。

使用 west：

```sh
# From the root of the zephyr repository
west build -b mps2/an521/cpu0/ns samples/hello_world
west build -t bl2_rom_report
```

使用 CMake 与 Ninja：

```sh
# From the root of the zephyr repository
# Use cmake to configure a Ninja-based buildsystem:
cmake -Bbuild -GNinja -DBOARD=mps2/an521/cpu0/ns samples/hello_world

# Now run the build tool on the generated build system:
ninja -Cbuild bl2_rom_report
```


译注核对来源：[modules/trusted-firmware-m/CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/CMakeLists.txt)、[modules/trusted-firmware-m/Kconfig.tfm](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm)。

本仓库的[对应源码](../../../modules/trusted-firmware-m/CMakeLists.txt)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="tf-m-build-system"></a>
<a id="tfm-build-system"></a>
<a id="images-created-by-the-tf-m-build"></a>
<a id="signing-images"></a>
<a id="output-files"></a>
<a id="id1"></a>
<a id="custom-cmake-arguments"></a>
<a id="footprint-and-memory-usage"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：TFM环境与硬件要求](P003_TFM环境与硬件要求.md) · [本模块主线目录](../reading/tfm.md) · [全部主线](../reading/README.md) · [下一篇：TFM与Zephyr集成](P005_TFM与Zephyr集成.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P003_TFM环境与硬件要求.md) · [返回大纲](大纲.md) · [下一章](P005_TFM与Zephyr集成.md)

</details>

<!-- reading-navigation:end -->
