---
id: learning.zephyr-docs.hardware.soc-porting
title: SoC移植指南
kind: tutorial
status: maintained
domains: [zephyr, soc, porting]
source_url: https://docs.zephyrproject.org/latest/hardware/porting/soc_porting.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="soc-porting-guide"></a>

# 第2章\_SoC移植指南

原文：[SoC Porting Guide](https://docs.zephyrproject.org/latest/hardware/porting/soc_porting.html)。读取日期：2026-10-12，`latest`。

本页介绍如何为新的 **片上系统（System on Chip，SoC）** 增加 Zephyr 支持，既适用于贡献到上游，也适用于保存在自己的仓库中。

## 2.1\_SoC定义与前置概念

阅读前应了解 Zephyr 的开发板概念。硬件支持层次见[开发板移植指南](P001_开发板移植指南.md)。SoC 移植中主要术语如下：

| 术语 | 含义 |
| --- | --- |
| SoC | 开发板 **中央处理器（Central Processing Unit，CPU）** 所属的具体片上系统。 |
| SoC 系列（series） | 一组关系紧密的 SoC。 |
| SoC 家族（family） | 具有相似特征、更大范围的一组 SoC。 |
| CPU 簇（cluster） | 一个或多个 CPU 核组成的簇。 |
| CPU 核（core） | 某种架构的具体 CPU 实例。 |
| 架构（architecture） | 指令集架构。 |

如果架构本身尚未支持，参见[架构移植指南](https://docs.zephyrproject.org/latest/hardware/porting/arch.html)。

## 2.2\_创建SoC目录

每个 SoC 必须有唯一名称。使用厂商的正式名称，并检查是否已经存在。同名 SoC 可能已由他人贡献；这种情况下应改进已有支持，而不是另建一份。

`list_hardware` 脚本可列出 Zephyr 已知 SoC。例如在 Zephyr 根目录执行 `./scripts/list_hardware.py --soc-root=. --socs`，查看已使用的名称。

创建 `zephyr/soc/<VENDOR>/soc1`。提交上游时，`<VENDOR>` 厂商子目录必需；放在自己的仓库时，`<your-repo>/soc` 下的目录层次可以自行安排。厂商名必须匹配 `dts/bindings/vendor-prefixes.txt` 中的前缀；尚未收录时应新增前缀。

SoC 目录名不必等于 SoC 名，一个目录可定义多个 SoC。Zephyr 经常把 SoC 放在公共家族或系列目录树的子目录中。基本结构如下：

```text
soc/<VENDOR>/<soc-name>
├── soc.yml
├── soc.h
├── CMakeLists.txt
├── Kconfig
├── Kconfig.soc
└── Kconfig.defconfig
```

把 `<soc-name>` 替换成实际名称。必需文件如下：

| 文件 | 用途 |
| --- | --- |
| `soc.yml` | 高层元数据，包括 SoC 名、一个或多个 CPU 簇（如有）、所属系列及系列所属家族。 |
| `soc.h` | 描述 SoC 或提供配置宏，常由驱动、子系统、开发板和其他 Zephyr 源码包含。 |
| `Kconfig.soc` | 定义 `config SOC_<soc-name>`，并为 `SOC` 提供 SoC 名。YAML 若描述家族和系列，此处也须定义。不得选择 SoC 配置树之外的符号；通用 Zephyr 设置放在 `Kconfig`。 |
| `CMakeLists.txt` | 由构建系统加载，设置额外包含路径、源文件，并定义使用的基础链接脚本。 |

可选的 `Kconfig`、`Kconfig.defconfig` 使用 Kconfig 格式，选择架构、可用外设及相关默认值。

## 2.3\_编写soc.yml

YAML 描述 SoC 家族、系列和具体 SoC 的高层结构，详细硬件描述和配置由设备树及 Kconfig 完成。仅含一个 SoC 的最小结构如下：

```yaml
socs:
  - name: <soc1>
```

同一目录可以包含多个 SoC；属于共同家族或系列时，推荐放在共同目录树下。多个系列和 SoC 可这样描述：

```yaml
family:
  - name: <family-name>
    series:
      - name: <series-1-name>
        socs:
          - name: <soc1>
            cpuclusters:
              - name: <coreA>
              - name: <coreB>
                ...
          - name: <soc2>
      - name: <series-2-name>
        ...
```

## 2.4\_编写SoC设备树

SoC 的设备树包含文件位于 `<zephyr-repo>/dts/<ARCH>/<VENDOR>`。`dts/<ARCH>/<VENDOR>/<soc>.dtsi` 用 **设备树源文件（Devicetree Source，DTS）** 格式描述 SoC 硬件，所有使用该 SoC 的开发板都必须包含它。

如果已有更高层的 `<arch>.dtsi`，可以先将它包含进 `<soc>.dtsi`。原文提供的整体骨架如下：

```dts
#include <arch>/<arch>.dtsi

/ {
        chosen {
                /* common chosen settings for your SoC */
        };

        cpus {
                #address-cells = <m>;
                #size-cells = <n>;

                cpu@0 {
                device_type = "cpu";
                compatible = "<compatibles>";
                /* ... your CPU definitions ... */
        };

        soc {
                /* Your SoC definitions and peripherals */
                /* such as ram, clock, buses, peripherals. */
        };
};
```

> 译注：这是带占位符的原文骨架，不能直接编译。原文缺少关闭 `cpus` 节点的一行 `};`，应放在 `cpu@0` 的结束符之后、`soc {` 之前，使 `cpus` 与 `soc` 同属根节点。`#include <arch>/<arch>.dtsi` 也只是路径示意，应换成实际有效的 include 写法；地址单元数、compatible、CPU 定义和外设均须填写真实值。这里保留原文代码以便核对。

为使目录更清晰，可把多个 `<VENDOR>/<soc>.dtsi` 按系列放在子目录，例如 `<VENDOR>/<SERIES>/<soc>.dtsi`。

### 2.4.1\_多个CPU簇

设备树反映硬件。不同 CPU 簇能访问的内存空间与外设可能有很大差异，因此通常每个簇有自己的 `.dtsi`。

CPU 簇文件应采用 `<soc>_<cluster>.dtsi` 命名；内容形式类似不含 CPU 簇划分的普通 SoC `.dtsi`。

## 2.5\_编写Kconfig文件

为 SoC 编译应用前，需要提供相应软件配置。取值规则见[设置配置值](../kconfig/P003_设置配置值.md)。SoC 目录有一个必需 Kconfig 文件和两个可选文件：

```text
soc/<vendor>/<your soc>
├── Kconfig.soc
├── Kconfig
└── Kconfig.defconfig
```

### 2.5.1\_Kconfig.soc

此文件可同时被 Zephyr 与 Sysbuild 的 Kconfig 树包含，用来选择 SoC 家族、系列及其他 SoC 相关符号，有时还包括 `SOC_PART_NUMBER`。不得选择可复用 SoC 配置树之外的符号。

典型内容如下：

```kconfig
config SOC_FAMILY_<SOC_FAMILY_NAME>
        bool

config SOC_SERIES_<SOC_SERIES_NAME>
        bool
        select SOC_FAMILY_<SOC_FAMILY_NAME>

config SOC_<SOC_NAME>
        bool
        select SOC_SERIES_<SOC_SERIES_NAME>

config SOC_FAMILY
        default "<soc_family_name>" if SOC_FAMILY_<SOC_FAMILY_NAME>

config SOC_SERIES
        default "<soc_series_name>" if SOC_SERIES_<SOC_SERIES_NAME>

config SOC
        default "<soc_name>" if SOC_<SOC_NAME>
```

`SOC_NAME`、`SOC_SERIES_NAME`、`SOC_FAMILY_NAME` 分别是 SoC、系列、家族名称的纯大写形式。`soc.yml` 没有描述的层次，不应出现在 `Kconfig.soc` 中。

`SOC`、`SOC_SERIES`、`SOC_FAMILY` 已全局定义为字符串，此文件只提供默认字符串值，不要重复声明类型。字符串值必须与 `soc.yml` 的名称完全匹配。

构建系统允许 `soc_name`、`soc_series_name`、`soc_family_name` 使用不同大小写组合，但提交到 Zephyr 上游时，这些名称必须是对应 Kconfig 名称的纯小写形式。

### 2.5.2\_Kconfig

此文件由 `soc/Kconfig` 包含，可增加当前 SoC 专用配置。硬件能力常通过 `HAS_<support>` 形式的符号表示，例如：

```kconfig
config SOC_<SOC_NAME>
        select ARM
        select CPU_HAS_FPU
```

如果只是为 Zephyr 已有符号修改默认值，应使用 `Kconfig.defconfig`。

### 2.5.3\_Kconfig.defconfig

此文件提供 SoC 专用默认值，并非每个 SoC 都需要。整个文件应放在 `if SOC_<SOC_NAME>` / `endif` 或 `if SOC_SERIES_<SERIES_NAME>` / `endif` 中，例如：

```kconfig
if SOC_<SOC_NAME>

config NUM_IRQS
        default 32

endif # SOC_<SOC_NAME>
```

### 2.5.4\_多个CPU簇的符号

CPU 簇还需要在 `Kconfig.soc` 中提供额外符号，通常为 `SOC_<SOC_NAME>_<CLUSTER>`。例如 `soc1` 有 `clusterA`、`clusterB` 两个簇：

```kconfig
config SOC_SOC1_CLUSTERA
        bool
        select SOC_SOC1

config SOC_SOC1_CLUSTERB
        bool
        select SOC_SOC1
```

两个簇的选择都会选中基础 SoC 符号 `SOC_SOC1`。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：开发板移植指南](P001_开发板移植指南.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：设备驱动模型](P003_设备驱动模型.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：开发板移植指南](P001_开发板移植指南.md) · [下一章：设备驱动模型](P003_设备驱动模型.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
