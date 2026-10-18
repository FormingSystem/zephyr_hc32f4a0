---
id: learning.zephyr-docs.boards-espressif.page-4
title: Using Espressif QEMU
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/espressif/common/qemu.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="using-espressif-qemu"></a>

# 第4章\_使用乐鑫QEMU（Using Espressif QEMU）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/espressif/common/qemu.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

乐鑫开发板可在Espressif维护的QEMU分支中运行，进行无需硬件的本地测试。[`CONFIG_ESPRESSIF_QEMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPRESSIF_QEMU)会生成合并的SPI闪存镜像，启用它时还会选择隐藏的开发板标记[`CONFIG_ESPRESSIF_QEMU_TARGET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPRESSIF_QEMU_TARGET)。只有开发板接入`espressif_qemu`仿真平台（Emu Platform）后，才有`west build -t run`目标；下列DevKitC开发板通过共享的`board.cmake`辅助文件完成接入。（[乐鑫QEMU分支（Fork）](https://github.com/espressif/qemu)）

参考DevKitC开发板有两种启用乐鑫QEMU的方式：


1. 在硬件开发板目标上指定`-DCONFIG_ESPRESSIF_QEMU=y`来启用。同一固件镜像随后可以烧录到实板（不使用该选项），也可以在QEMU中运行。基于受支持SoC的其他开发板也可设置此Kconfig选项来导出闪存布局，但要使用`-t run`，还需同样通过`SUPPORTED_EMU_PLATFORMS`接入`espressif_qemu`。
2. 使用下列参考DevKitC目标的开发板变体（Board Variant），即`/qemu`限定符。变体defconfig已设置[`CONFIG_ESPRESSIF_QEMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPRESSIF_QEMU)，无需额外指定`-D`，可用于本地及持续集成（CI）的`west build -t run`流程。Twister仿真方面，尚未接入Espressif QEMU元数据；应将`/qemu`视为开发板标识加仿真平台，不能直接替代标准`qemu_*` Twister仿真。

<a id="supported-socs-and-boards"></a>

## 受支持的SoC与开发板（Supported SoCs and Boards）

<table>
<tr>
<th>片上系统（SoC）</th>
<th>硬件开发板（Hardware Board）</th>
<th>QEMU变体，持续集成（CI）</th>
<th>QEMU可执行程序（Binary）</th>
<th><code>-machine</code></th>
</tr>
<tr>
<td>ESP32</td>
<td><code>esp32_devkitc/esp32/procpu</code></td>
<td><code>esp32_devkitc/esp32/procpu/qemu</code></td>
<td><code>qemu-system-xtensa</code></td>
<td><code>esp32</code></td>
</tr>
<tr>
<td>ESP32-S3</td>
<td><code>esp32s3_devkitc/esp32s3/procpu</code></td>
<td><code>esp32s3_devkitc/esp32s3/procpu/qemu</code></td>
<td><code>qemu-system-xtensa</code></td>
<td><code>esp32s3</code></td>
</tr>
<tr>
<td>ESP32-C3</td>
<td><code>esp32c3_devkitc/esp32c3</code></td>
<td><code>esp32c3_devkitc/esp32c3/qemu</code></td>
<td><code>qemu-system-riscv32</code></td>
<td><code>esp32c3</code></td>
</tr>
<tr>
<td>ESP32-C6</td>
<td><code>esp32c6_devkitc/esp32c6/hpcore</code></td>
<td><code>esp32c6_devkitc/esp32c6/hpcore/qemu</code></td>
<td><code>qemu-system-riscv32</code></td>
<td><code>esp32c6</code></td>
</tr>
</table>

ESP32-C3及ESP32-C6需要`-icount 3`，运行目标会自动添加。它们不支持自由运行模式（Free-Running Mode）。

注意（Note）

截至`esp-develop-9.2.2-20260417`，乐鑫QEMU预构建发行版仅包含esp32、esp32s3及esp32c3。ESP32-C6支持已通过提交[https://github.com/espressif/qemu/commit/febae182e132e4055529be423a818225ebddaa3a](https://github.com/espressif/qemu/commit/febae182e132e4055529be423a818225ebddaa3a)合入乐鑫`esp-develop`分支，但尚未包含在公开发行的二进制程序中。要运行ESP32-C6，请从`esp-develop`分支构建QEMU。

<a id="emulated-peripherals"></a>

## 仿真的外设（Emulated Peripherals）

各SoC能力见[乐鑫QEMU功能矩阵（Feature Matrix）](https://github.com/espressif/esp-toolchain-docs/blob/main/qemu/README.md)。该矩阵尚无ESP32-C6列；下表C6取值依据当前`esp-develop`中的`esp32c6`机器实现，而非直接复制ESP32-C3。

<a id="usable-in-zephyr-on-qemu-devkitc-boards"></a>

### 可在Zephyr的`/qemu` DevKitC开发板中使用

<table>
<tr>
<th>外设（Peripheral）</th>
<th>ESP32</th>
<th>ESP32-S3</th>
<th>ESP32-C3</th>
<th>ESP32-C6</th>
</tr>
<tr>
<td>UART控制台（Console）</td>
<td>是（yes）</td>
<td>是（yes）</td>
<td>是（yes）</td>
<td>是（yes）</td>
</tr>
<tr>
<td>NOR闪存，SPI加存储器管理单元（MMU）</td>
<td>是（yes）</td>
<td>是（yes）</td>
<td>是（yes）</td>
<td>是（yes）</td>
</tr>
<tr>
<td>电子熔丝（eFuse）</td>
<td>支持，自动使用ECO3镜像</td>
<td>是（yes）</td>
<td>是（yes）</td>
<td>是（yes）</td>
</tr>
<tr>
<td>随机数／真随机数发生器（RNG／TRNG）</td>
<td>是（yes）</td>
<td>是（yes）</td>
<td>是（yes）</td>
<td>否（no）</td>
</tr>
<tr>
<td>AES／SHA／RSA密码运算（Crypto）</td>
<td>是（yes）</td>
<td>支持，另含HMAC及数字签名（DS）</td>
<td>支持，另含HMAC及数字签名（DS）</td>
<td>仅支持SHA</td>
</tr>
<tr>
<td>定时器组／系统定时器（Timer Groups／SysTimer）</td>
<td>是（yes）</td>
<td>是（yes）</td>
<td>是（yes）</td>
<td>是（yes）</td>
</tr>
<tr>
<td>双线汽车接口（TWAI）／控制器局域网（CAN）</td>
<td>已建模（modeled）</td>
<td>已建模（modeled）</td>
<td>已建模（modeled）</td>
<td>否（no）</td>
</tr>
<tr>
<td>伪静态随机存储器（PSRAM），<code>-m</code>选项</td>
<td>四线外设接口（QPI），2M／4M</td>
<td>四线／八线外设接口（QPI／OPI），2M至32M</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td>通用直接存储器访问（GDMA）</td>
<td>无Zephyr冒烟测试（Smoke Test）</td>
<td>支持，SoC层面</td>
<td>支持，SoC层面</td>
<td>支持，SoC层面</td>
</tr>
</table>

<a id="not-emulated-disabled-in-qemu-device-trees"></a>

### 未仿真的外设，在`/qemu`设备树中禁用

Wi-Fi、蓝牙、USB、通用SPI、I2C、I2S、远程控制外设RMT、GPIO矩阵／IOMUX、ADC／DAC、触摸、MCPWM、脉冲计数器、超低功耗处理器ULP及开发板GPIO按键均未仿真。LEDC仅在ESP32上仿真；ESP32-S3未仿真SD／MMC。ESP32-C6还需禁用TRNG、AES及高性能／低功耗域邮箱`mbox0`，保留SHA。

依赖这些外设的测试无法在QEMU中运行。

<a id="qemu-variant-device-tree"></a>

## QEMU变体设备树（Variant Device Tree）

硬件DevKitC目标保留完整设备树。`/qemu`变体包含同一硬件`*.dts`，再对QEMU未建模的节点覆盖`status = "disabled"`，或使用`/delete-node/`删除：


- `boards/espressif/esp32_devkitc/esp32_devkitc_procpu_qemu.dts`
- `boards/espressif/esp32s3_devkitc/esp32s3_devkitc_procpu_qemu.dts`
- `boards/espressif/esp32c3_devkitc/esp32c3_devkitc_qemu.dts`
- `boards/espressif/esp32c6_devkitc/esp32c6_devkitc_hpcore_qemu.dts`

公共覆盖文件禁用Wi-Fi、蓝牙、I2C、I2S、通用SPI、ADC及未仿真的PWM相关模块，删除GPIO按键节点，并清除不支持的chosen属性。Xtensa变体还禁用触摸、脉冲计数器及MCPWM节点。ESP32-S3额外禁用第二组I2C／SPI／I2S实例、USB Serial／JTAG及OTG、LEDC、SD／MMC、温度传感器和LCD／CAM控制器。ESP32-C3禁用USB Serial／JTAG、LEDC及温度传感器。ESP32-C6禁用IEEE 802.15.4、LP UART、MCPWM、脉冲计数器、TRNG及`zephyr,entropy`、AES和`mbox0`，仍保留SHA。

UART、闪存分区、定时器组及看门狗节点仍可用于冒烟测试，例如`samples/hello_world`。ESP32／S3／C3保留TRNG及完整密码模块，ESP32-C6仅保留SHA。GPIO控制器节点和`CONFIG_GPIO=y`必须保持启用，因为乐鑫UART驱动为配置引脚复用会选择GPIO驱动；尝试禁用会导致Kconfig依赖错误。这是启动所需基础功能，并不表示QEMU已实现应用GPIO或GPIO矩阵；设备树中的GPIO按键节点会被移除。

<a id="automatic-vs-manual-qemu-flags"></a>

### 自动添加与手动设置的QEMU参数（Automatic vs Manual Flags）

启用[`CONFIG_ESPRESSIF_QEMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPRESSIF_QEMU)后，`west build -t run`目标会自动添加以下参数：


- ESP32-C3及ESP32-C6添加`-icount 3`
- ESP32添加ECO3电子熔丝（eFuse）镜像，见闪存容量及ESP32芯片版本章节（[闪存容量（Flash Size）](#flash-size)；[ESP32芯片版本（Chip Revision）](#esp32-chip-revision)）
- `-drive file=…/flash_image.bin,if=mtd,format=raw`
- 设置[`CONFIG_ESP_SPIRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_SPIRAM)时添加`-m <size>`；容量来自[`CONFIG_ESP_SPIRAM_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_SPIRAM_SIZE)，默认值由设备树`psram0`节点的`size`属性提供
- ESP32-S3设置[`CONFIG_SPIRAM_MODE_OCT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPIRAM_MODE_OCT)时，添加`-global driver=ssi_psram,property=is_octal,value=true`

禁用看门狗、在ESP32上使用SD卡等可选情况，可通过`QEMU_EXTRA_FLAGS`环境变量设置。

<a id="installing-espressif-qemu"></a>

## 安装乐鑫QEMU（Installing Espressif QEMU）

从[https://github.com/espressif/qemu/releases](https://github.com/espressif/qemu/releases)下载Xtensa及RISC-V预构建软件包。

示例：Linux x86_64，发行版`esp-develop-9.2.2-20260417`：

```text
mkdir -p ~/Downloads ~/opt
cd ~/Downloads
wget https://github.com/espressif/qemu/releases/download/esp-develop-9.2.2-20260417/qemu-xtensa-softmmu-esp_develop_9.2.2_20260417-x86_64-linux-gnu.tar.xz
wget https://github.com/espressif/qemu/releases/download/esp-develop-9.2.2-20260417/qemu-riscv32-softmmu-esp_develop_9.2.2_20260417-x86_64-linux-gnu.tar.xz
tar -xf qemu-xtensa-softmmu-*.tar.xz -C ~/opt --one-top-level=qemu-xtensa-softmmu
tar -xf qemu-riscv32-softmmu-*.tar.xz -C ~/opt --one-top-level=qemu-riscv32-softmmu
```

将两个`bin`目录都加入`PATH`，或将`ESPRESSIF_QEMU_PATH`／`QEMU_BIN_PATH`设为相应平台格式的路径列表，包含目标SoC所需目录。不提供`-machine esp*`的通用发行版QEMU不能使用。

CMake配置时，按`ESPRESSIF_QEMU_PATH`、`QEMU_BIN_PATH`、`PATH`的顺序查找`qemu-system-xtensa`／`qemu-system-riscv32`，逐个执行`-machine help`探测，选择第一个实现目标SoC机器类型的程序。这样会跳过Zephyr SDK的hosttools中不含乐鑫机器类型的上游QEMU。选中的可执行程序会按以下格式输出：

```text
-- Espressif QEMU: /home/user/opt/qemu-xtensa-softmmu/qemu/bin/qemu-system-xtensa (-machine esp32)
```

查找发生在配置阶段，因此构建后安装QEMU或修改`ESPRESSIF_QEMU_PATH`，需要重新运行CMake，可使用`west build --pristine`。

<a id="building-and-running-simple-boot"></a>

## 构建与运行：简单启动（Simple Boot）

除非指定`--sysbuild`或在west配置中设置`build.sysbuild`，`west build`默认不使用sysbuild；普通构建生成不含MCUboot的Simple Boot镜像。下方的`--no-sysbuild`明确选择这种方式，同时覆盖west中的`build.sysbuild=true`配置。

显式启用：硬件开发板加CMake缓存项（Cache Entry）：

```text
west build -b esp32_devkitc/esp32/procpu samples/hello_world \
  --no-sysbuild --pristine \
  -- -DCONFIG_ESPRESSIF_QEMU=y

west build -t run
```

QEMU开发板变体，由defconfig提供[`CONFIG_ESPRESSIF_QEMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPRESSIF_QEMU)：

```text
west build -b esp32_devkitc/esp32/procpu/qemu samples/hello_world \
  --no-sysbuild --pristine

west build -t run
```

构建生成合并SPI镜像`build/zephyr/flash_image.bin`，并注册`espressif_qemu`仿真平台：`run_espressif_qemu`／`debugserver_espressif_qemu`分别映射为`west build -t run`／`debugserver`。ESP32还会生成`build/zephyr/qemu_efuse_eco3.bin`并传给QEMU。等价手动调用如下：

```text
qemu-system-xtensa -nographic -machine esp32 \
  -drive file=build/zephyr/qemu_efuse_eco3.bin,if=none,format=raw,id=efuse \
  -global driver=nvram.esp32.efuse,property=drive,value=efuse \
  -drive file=build/zephyr/flash_image.bin,if=mtd,format=raw
```

ESP32-C3显式启用示例：

```text
west build -b esp32c3_devkitc/esp32c3 samples/hello_world \
  --no-sysbuild --pristine \
  -- -DCONFIG_ESPRESSIF_QEMU=y
west build -t run
```

ESP32-C3变体，无需`-D`：

```text
west build -b esp32c3_devkitc/esp32c3/qemu samples/hello_world \
  --no-sysbuild --pristine
west build -t run
# or:
qemu-system-riscv32 -nographic -icount 3 -machine esp32c3 \
  -drive file=build/zephyr/flash_image.bin,if=mtd,format=raw
```

<a id="mcuboot-sysbuild"></a>

## MCUboot与系统构建（Sysbuild）

使用sysbuild时，[`CONFIG_ESPRESSIF_QEMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPRESSIF_QEMU)将MCUboot的`boot_partition`及已签名应用的`slot0_partition`合并到同一闪存镜像：

```text
west build -b esp32_devkitc/esp32/procpu samples/hello_world \
  --sysbuild --pristine \
  -- -DCONFIG_ESPRESSIF_QEMU=y

west build --domain hello_world -t run
```

这里必须指定`--domain`：`run`由应用镜像定义，sysbuild顶层构建没有此目标。镜像写入`build/<app>/zephyr/flash_image.bin`，而不是`build/zephyr/`。

合并过程读取引导加载程序构建域的`../mcuboot/zephyr/zephyr.bin`。Sysbuild将每个镜像作为独立外部项目加入构建，因此只要应用及MCUboot两个ExternalProject目标都存在，这些DevKitC开发板的`sysbuild.cmake`就始终让应用在MCUboot之后构建。此依赖不以[`CONFIG_ESPRESSIF_QEMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPRESSIF_QEMU)为条件，因为在sysbuild的CMake上下文中无法可靠读取该配置。没有此顺序时，两域并行构建，合并过程可能读到尚未完整生成的引导加载程序二进制文件。

在非sysbuild构建中设置[`CONFIG_BOOTLOADER_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOOTLOADER_MCUBOOT)，不会在构建树中生成引导加载程序二进制文件；实板使用时通常已烧录MCUboot。对于QEMU，应使用`--sysbuild`，或通过`-DESPRESSIF_QEMU_MCUBOOT_BIN=<path to mcuboot zephyr.bin>`传入现有引导加载程序镜像。该参数路径必须为绝对路径，因为合并命令在构建目录中运行。【译注：这里要求的是执行时解析出的实际路径，并非写死某台机器上的仓库位置。】

<a id="gdb-debugging"></a>

## GDB调试（GDB Debugging）

启动QEMU，使CPU保持复位，并在1234端口提供GDB桩（GDB Stub）：

```text
west build -t debugserver
```

使用sysbuild时，与`run`相同，需要添加`--domain <app>`。然后在另一个终端使用Zephyr SDK附带的GDB连接：

```text
$ZEPHYR_SDK_INSTALL_DIR/gnu/xtensa-espressif_esp32_zephyr-elf/bin/xtensa-espressif_esp32_zephyr-elf-gdb \
  build/zephyr/zephyr.elf \
  -ex "target remote :1234" \
  -ex "tb main" -ex "c"
```

RISC-V SoC，即ESP32-C3和ESP32-C6，改用`gnu/riscv64-zephyr-elf/bin/riscv64-zephyr-elf-gdb`。如果`PATH`上已有ESP-IDF环境，也可使用ESP-IDF工具链的GDB：`xtensa-esp32-elf-gdb`或`riscv32-esp-elf-gdb`。

<a id="advanced-qemu-arguments"></a>

## 高级QEMU参数（Advanced Arguments）

可通过`QEMU_EXTRA_FLAGS`环境变量注入额外参数，以空格分隔。该变量在CMake配置时读取，应在首次构建前设置；之后修改时需重新运行CMake。以下选项不会自动添加：


- 禁用定时器组（TG）看门狗：`-global driver=timer.esp32.timg,property=wdt_disable,value=true`；ESP32-S3、ESP32-C3及ESP32-C6使用属性名称`timer.esp32c3.timg`
- SD／MMC，仅限ESP32：`-drive file=sdcard.img,if=sd,format=raw`
- 自定义eFuse存储：配置时指定`-DESPRESSIF_QEMU_EFUSE_HEX_FILE=/path/to/efuse.hex`。十六进制文件允许空白字符。构建过程将其复制到构建目录，使用Python解码，再把所得二进制文件传给机器的eFuse设备。不指定时，ESP32使用内置ECO3镜像，其他SoC不附加eFuse驱动器。此过程不写入源码树。

  eFuse布局及绑带启动模式（Strap Modes）见[https://github.com/espressif/esp-toolchain-docs/tree/main/qemu](https://github.com/espressif/esp-toolchain-docs/tree/main/qemu)下各SoC页面。

<a id="psram-automatic-when-spiram-is-enabled"></a>

### PSRAM：启用SPIRAM时自动配置

启用[`CONFIG_ESP_SPIRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_SPIRAM)时，CMake添加`-m <size>`；`<size>`由[`CONFIG_ESP_SPIRAM_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_SPIRAM_SIZE)推导，即字节数除以1 MiB，再加后缀M。不支持的容量会使配置失败，不应传入仅部分支持的`-m`取值。ESP32的`/qemu`变体将`psram0`限制为4M，因为硬件WROVER N4R8设备树默认是8M。

文档列出的QEMU支持容量：


- ESP32：2M、4M；PSRAM MMU尚未完整仿真
- ESP32-S3：2M、4M、8M、16M或32M；启用`CONFIG_SPIRAM_MODE_OCT=y`时，八线（OPI）模式还会添加`ssi_psram`的`is_octal`全局参数

必要时可通过`QEMU_EXTRA_FLAGS`覆盖或补充参数。

<a id="flash-size"></a>

## 闪存容量（Flash Size）

合并镜像会填充到设备树中`zephyr,flash`指定的闪存容量，使SPI闪存头与QEMU存储技术设备（MTD）容量一致。乐鑫QEMU支持2、4、8及16 MB，应使用闪存容量为这些值之一的开发板或覆盖文件。

<a id="esp32-chip-revision"></a>

## ESP32芯片版本（Chip Revision）

默认QEMU eFuse报告ESP32版本0，除非启用[`CONFIG_ESP32_USE_UNSUPPORTED_REVISION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_USE_UNSUPPORTED_REVISION)，否则Zephyr会拒绝该版本。启用[`CONFIG_ESPRESSIF_QEMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPRESSIF_QEMU)后，`run`／`debugserver`目标会自动附加设置了`CHIP_VER_REV1`及`CHIP_VER_REV2`的ECO3 eFuse镜像，使客户机报告芯片版本v3.0。

配置时，在构建目录下写入ECO3十六进制数据，再通过Python解码为`build/zephyr/qemu_efuse_eco3.bin`。可以在配置时通过`-DESPRESSIF_QEMU_EFUSE_HEX_FILE=...`覆盖；也可在后续`west build`或`west build -t run`中传入同一`-D`，触发CMake重新配置。只设置环境变量不够，因为该路径仅在CMake配置阶段读取。布局对应[模拟ESP32 ECO3（Emulating ESP32 ECO3）](https://github.com/espressif/esp-toolchain-docs/blob/main/qemu/esp32/README.md#emulating-esp32-eco3)。

等价手动QEMU调用：

```text
qemu-system-xtensa -nographic -machine esp32 \
  -drive file=build/zephyr/qemu_efuse_eco3.bin,if=none,format=raw,id=efuse \
  -global driver=nvram.esp32.efuse,property=drive,value=efuse \
  -drive file=build/zephyr/flash_image.bin,if=mtd,format=raw
```

## 译注

此页来自官方latest公共文档，已重新下载核对来源摘要。ESP32-C6的QEMU发行状态、自动添加参数、芯片eFuse版本以及Twister集成限制均依原文所述版本语境保留，未执行仿真验证。源码与本地文档链接使用相对路径；原文要求MCUboot镜像参数为绝对路径，是运行时工具参数约束，不能据此写死作者的仓库位置。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [README.md](https://github.com/espressif/esp-toolchain-docs/blob/main/qemu/esp32/README.md#emulating-esp32-eco3)：页面可访问，但未确认目标片段。

---

[上一章](P003_OpenOCD_Debugging.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_ESP32_Features.md)
