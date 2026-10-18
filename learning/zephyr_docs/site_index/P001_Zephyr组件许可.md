---
id: learning.zephyr-docs.site-index.page-1
title: Zephyr组件许可
kind: reference
status: maintained
domains: [zephyr, documentation]
source_url: https://docs.zephyrproject.org/latest/LICENSING.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="licensing-of-zephyr-project-components"></a>

<a id="zephyr-licensing"></a>

# 第1章\_Zephyr项目组件许可（Licensing of Zephyr Project Components）

原文：[官方页面](https://docs.zephyrproject.org/latest/LICENSING.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

Zephyr整体采用Apache 2.0许可证，但也引入或复用了少量采用其他许可证的软件包、脚本及文件。部分文件无法添加许可头，因此遵循REUSE规范，在仓库根目录的[REUSE.toml](https://github.com/zephyrproject-rtos/zephyr/blob/main/REUSE.toml)中以机器可读形式集中声明许可信息。（[Apache 2.0许可证（License）](https://github.com/zephyrproject-rtos/zephyr/blob/main/LICENSE)；[REUSE规范（Specification）](https://reuse.software/spec/)）

以下章节由这些元数据自动生成，因而反映源码树的实际状态。若要添加、更新或移除条目，应编辑[REUSE.toml](https://github.com/zephyrproject-rtos/zephyr/blob/main/REUSE.toml)中对应的[[annotations]]块，而非本页。见[贡献外部组件（Contributing External Components）](../contributing/P012_外部组件贡献.md#external-contributions)。

注意（Note）

本页仅列出许可例外，不定义Zephyr项目自身的许可证。项目许可证为Apache 2.0，见仓库根目录[LICENSE](https://github.com/zephyrproject-rtos/zephyr/blob/main/LICENSE)文件。

<a id="documented-components"></a>

已记录的组件（Documented Components）


- <a id="id1"></a>

  [Bootstrap JavaScript及CSS文件](#bootstrap-javascript-and-css-files)
- <a id="id2"></a>

  [博世BMI08x传感器配置文件（Bosch BMI08x Sensor Configuration File）](#bosch-bmi08x-sensor-configuration-file)
- <a id="id3"></a>

  [Coccinelle语义补丁脚本（Coccinelle Scripts）](#coccinelle-scripts)
- <a id="id4"></a>

  [持续集成脚本（Continuous Integration Scripts）](#continuous-integration-scripts)
- <a id="id5"></a>

  [Doxygen Awesome CSS主题文件](#doxygen-awesome-css-theme-files)
- <a id="id6"></a>

  [ENE KB1200_EVB开发板OpenOCD配置](#ene-kb1200-evb-board-openocd-configuration)
- <a id="id7"></a>

  [用户空间文件系统（FUSE）接口定义头文件](#fuse-interface-definition-header-file)
- <a id="id8"></a>

  [GCOV覆盖率头文件（Coverage Header File）](#gcov-coverage-header-file)
- <a id="id9"></a>

  [getopt命令行解析文件（Command-line Parsing Files）](#getopt-command-line-parsing-files)
- <a id="id10"></a>

  [Godot文档主题文件（Documentation Theme Files）](#godot-documentation-theme-files)
- <a id="id11"></a>

  [HTTP解析器文件（HTTP Parser Files）](#http-parser-files)
- <a id="id12"></a>

  [Kconfiglib配置库（Configuration Library）](#kconfiglib-configuration-library)
- <a id="id13"></a>

  [littlefs文件系统配置文件](#littlefs-configuration-files)
- <a id="id14"></a>

  [最小C库（Minimal libc）的atoi文件](#minimal-libc-atoi-file)
- <a id="id15"></a>

  [最小C库（Minimal libc）的BSD字符串及转换文件](#minimal-libc-bsd-string-and-conversion-files)
- <a id="id16"></a>

  [Modern CMake的Sphinx域（Sphinx Domain）](#modern-cmake-sphinx-domain)
- <a id="id17"></a>

  [noUiSlider库](#nouislider-library)
- <a id="id18"></a>

  [开放可移植可信执行环境（OP-TEE）消息接口头文件](#op-tee-message-interface-headers)
- <a id="id19"></a>

  [OpenThread Spinel HDLC无线协处理器（RCP）主机接口文件](#openthread-spinel-hdlc-rcp-host-interface-files)
- <a id="id20"></a>

  [Popper.js库](#popper-js-library)
- <a id="id21"></a>

  [POSIX fnmatch文件](#posix-fnmatch-files)
- <a id="id22"></a>

  [POSIX sys/stat.h头文件](#posix-sys-stat-h-header)
- <a id="id23"></a>

  [Python设备树库（Devicetree Library）文件](#python-devicetree-library-files)
- <a id="id24"></a>

  [Python设备树库（Devicetree Library）测试文件](#python-devicetree-library-test-files)
- <a id="id25"></a>

  [RISC-V控制与状态寄存器（CSR）头文件](#risc-v-control-and-status-register-header)
- <a id="id26"></a>

  [RV32M1 VEGA开发板OpenOCD配置](#rv32m1-vega-board-openocd-configuration)
- <a id="id27"></a>

  [可信固件M（TF-M）安全分区示例文件](#tf-m-secure-partition-sample-files)
- <a id="id28"></a>

  [Thread-Metric实时操作系统（RTOS）测试套件源文件](#thread-metric-rtos-test-suite-source-files)
- <a id="id29"></a>

  [Tippy.js库](#tippy-js-library)
- <a id="id30"></a>

  [UF2转换脚本（Conversion Script）](#uf2-conversion-script)
- <a id="id31"></a>

  [USB设备协议栈头文件（USB Device Stack Headers）](#usb-device-stack-headers)
- <a id="id32"></a>

  [WireGuard虚拟专用网络（VPN）文件](#wireguard-vpn-files)
- <a id="id33"></a>

  [Xen虚拟机监控器（Hypervisor）接口文件](#xen-hypervisor-interface-files)
- <a id="id34"></a>

  [xoshiro128++伪随机数生成器（PRNG）](#xoshiro128-prng)
- <a id="id35"></a>

  [Xtensa启动汇编文件（Startup Assembly Files）](#xtensa-startup-assembly-files)

<a id="bootstrap-javascript-and-css-files"></a>

## [Bootstrap JavaScript及CSS文件](#id1)

来源（Origin）：

[getbootstrap.com](https://getbootstrap.com/)

许可证（License）：

[MIT](https://spdx.org/licenses/MIT.html)

仅由仪表板（Dashboard）工具使用，不链接进Zephyr固件镜像。

文件（Files，共2个）：


- [scripts/dashboard/static/css/bootstrap-chop.css](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dashboard/static/css/bootstrap-chop.css)
- [scripts/dashboard/static/js/bootstrap-chop.js](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dashboard/static/js/bootstrap-chop.js)

<a id="bosch-bmi08x-sensor-configuration-file"></a>

## [博世BMI08x传感器配置文件（Bosch BMI08x Sensor Configuration File）](#id2)

来源（Origin）：

[github.com/BoschSensortec/BMI08x-Sensor-API](https://github.com/BoschSensortec/BMI08x-Sensor-API)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

启用条件（Enabled by）：

[`CONFIG_BMI08X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BMI08X)

传感器配置数据仅在启用BMI08x驱动时编译进固件。

文件（Files，共1个）：


- [drivers/sensor/bosch/bmi08x/bmi08x_config_file.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi08x/bmi08x_config_file.h)

<a id="coccinelle-scripts"></a>

## [Coccinelle语义补丁脚本（Coccinelle Scripts）](#id3)

来源（Origin）：

[coccinelle.gitlabpages.inria.fr/website](https://coccinelle.gitlabpages.inria.fr/website/)

许可证（License）：

[GPL-2.0](https://spdx.org/licenses/GPL-2.0.html)

由转换C代码的工具Coccinelle使用，不链接进固件。

文件（Files，共8个）：


- [scripts/coccicheck](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccicheck)
- [scripts/coccinelle/array_size.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/array_size.cocci)
- [scripts/coccinelle/deref_null.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/deref_null.cocci)
- [scripts/coccinelle/mini_lock.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/mini_lock.cocci)
- [scripts/coccinelle/noderef.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/noderef.cocci)
- [scripts/coccinelle/returnvar.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/returnvar.cocci)
- [scripts/coccinelle/semicolon.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/semicolon.cocci)
- [scripts/coccinelle/unsigned_lesser_than_zero.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/unsigned_lesser_than_zero.cocci)

<a id="continuous-integration-scripts"></a>

## [持续集成脚本（Continuous Integration Scripts）](#id4)

来源（Origin）：

[www.kernel.org](https://www.kernel.org/)

许可证（License）：

[GPL-2.0](https://spdx.org/licenses/GPL-2.0.html)

用于持续集成（CI），不链接进固件。

文件（Files，共3个）：


- [scripts/checkpatch.pl](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/checkpatch.pl)
- [scripts/checkstack.pl](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/checkstack.pl)
- [scripts/spelling.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/spelling.txt)

<a id="doxygen-awesome-css-theme-files"></a>

## [Doxygen Awesome CSS主题文件](#id5)

来源（Origin）：

[github.com/jothepro/doxygen-awesome-css](https://github.com/jothepro/doxygen-awesome-css)

许可证（License）：

[MIT](https://spdx.org/licenses/MIT.html)

设置Doxygen API文档样式，不链接进固件。

文件（Files，共4个）：


- [doc/_doxygen/doxygen-awesome-darkmode-toggle.js](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_doxygen/doxygen-awesome-darkmode-toggle.js)
- [doc/_doxygen/doxygen-awesome-sidebar-only-darkmode-toggle.css](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_doxygen/doxygen-awesome-sidebar-only-darkmode-toggle.css)
- [doc/_doxygen/doxygen-awesome-sidebar-only.css](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_doxygen/doxygen-awesome-sidebar-only.css)
- [doc/_doxygen/doxygen-awesome.css](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_doxygen/doxygen-awesome.css)

<a id="ene-kb1200-evb-board-openocd-configuration"></a>

## [ENE KB1200_EVB开发板OpenOCD配置](#id6)

来源（Origin）：

[openocd.org](https://openocd.org/)

许可证（License）：

[GPL-2.0-or-later](https://spdx.org/licenses/GPL-2.0-or-later.html)

OpenOCD在编程及调试kb1200_evb开发板时使用，不链接进固件。

文件（Files，共1个）：


- [boards/ene/kb1200_evb/support/openocd.cfg](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ene/kb1200_evb/support/openocd.cfg)

<a id="fuse-interface-definition-header-file"></a>

## [用户空间文件系统（FUSE）接口定义头文件](#id7)

许可证（License）：

`GPL-2.0 WITH Linux-syscall-note OR BSD-2-Clause`

启用条件（Enabled by）：

[`CONFIG_FUSE_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FUSE_CLIENT)

从其双重许可中选择BSD-2-Clause许可证使用。仅在启用相应控制选项时构建。

文件（Files，共1个）：


- [subsys/fs/fuse_client/fuse_abi.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/fuse_client/fuse_abi.h)

<a id="gcov-coverage-header-file"></a>

## [GCOV覆盖率头文件（Coverage Header File）](#id8)

来源（Origin）：

[gcc.gnu.org](https://gcc.gnu.org/)

许可证（License）：

`GPL-3.0-or-later WITH GCC-exception-3.1`

启用条件（Enabled by）：

[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)

仅在启用GCOV覆盖率时链接进固件，适用GCC运行时库例外（GCC Runtime Library Exception）。

文件（Files，共1个）：


- [subsys/testsuite/coverage/coverage.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/coverage/coverage.h)

<a id="getopt-command-line-parsing-files"></a>

## [getopt命令行解析文件（Command-line Parsing Files）](#id9)

来源（Origin）：

[www.netbsd.org](https://www.netbsd.org/)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

启用条件（Enabled by）：

[`CONFIG_GETOPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GETOPT)

仅在启用getopt()支持时编译进固件。

文件（Files，共3个）：


- [lib/utils/getopt/README](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/getopt/README)
- [lib/utils/getopt/getopt.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/getopt/getopt.c)
- [lib/utils/getopt/getopt_long.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/getopt/getopt_long.c)

<a id="godot-documentation-theme-files"></a>

## [Godot文档主题文件（Documentation Theme Files）](#id10)

来源（Origin）：

[github.com/godotengine/godot-docs](https://github.com/godotengine/godot-docs)

许可证（License）：

[CC-BY-3.0](https://spdx.org/licenses/CC-BY-3.0.html)

定制文档渲染使用的Sphinx主题，不链接进固件。

文件（Files，共4个）：


- [doc/_static/css/custom.css](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_static/css/custom.css)
- [doc/_static/css/dark.css](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_static/css/dark.css)
- [doc/_static/css/light.css](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_static/css/light.css)
- [doc/_static/js/custom.js](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_static/js/custom.js)

<a id="http-parser-files"></a>

## [HTTP解析器文件（HTTP Parser Files）](#id11)

来源（Origin）：

[github.com/nodejs/http-parser](https://github.com/nodejs/http-parser)

许可证（License）：

[MIT](https://spdx.org/licenses/MIT.html)

启用条件（Enabled by）：

[`CONFIG_HTTP_PARSER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_PARSER)

仅在启用HTTP解析器时编译进固件。

文件（Files，共5个）：


- [include/zephyr/net/http/parser.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/http/parser.h)
- [include/zephyr/net/http/parser_state.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/http/parser_state.h)
- [include/zephyr/net/http/parser_url.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/http/parser_url.h)
- [subsys/net/lib/http/http_parser.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/http_parser.c)
- [subsys/net/lib/http/http_parser_url.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/http_parser_url.c)

<a id="kconfiglib-configuration-library"></a>

## [Kconfiglib配置库（Configuration Library）](#id12)

来源（Origin）：

[github.com/ulfalizer/Kconfiglib](https://github.com/ulfalizer/Kconfiglib)

许可证（License）：

[ISC](https://spdx.org/licenses/ISC.html)

构建时用于处理Kconfig文件，不链接进固件。

文件（Files，共4个）：


- [scripts/kconfig/guiconfig.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/kconfig/guiconfig.py)
- [scripts/kconfig/kconfig.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/kconfig/kconfig.py)
- [scripts/kconfig/kconfiglib.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/kconfig/kconfiglib.py)
- [scripts/kconfig/menuconfig.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/kconfig/menuconfig.py)

<a id="littlefs-configuration-files"></a>

## [littlefs文件系统配置文件](#id13)

来源（Origin）：

[github.com/littlefs-project/littlefs](https://github.com/littlefs-project/littlefs)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

启用条件（Enabled by）：

[`CONFIG_FILE_SYSTEM_LITTLEFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FILE_SYSTEM_LITTLEFS)

仅在启用littlefs文件系统时编译进固件。

文件（Files，共2个）：


- [modules/littlefs/zephyr_lfs_config.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/littlefs/zephyr_lfs_config.h)
- [modules/littlefs/zephyr_lfs_crc.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/littlefs/zephyr_lfs_crc.c)

<a id="minimal-libc-atoi-file"></a>

## [最小C库（Minimal libc）的atoi文件](#id14)

来源（Origin）：

[musl.libc.org](https://musl.libc.org/)

许可证（License）：

[MIT](https://spdx.org/licenses/MIT.html)

启用条件（Enabled by）：

[`CONFIG_MINIMAL_LIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MINIMAL_LIBC)

仅在选择最小C库（Minimal C Library）时编译进固件。

文件（Files，共1个）：


- [lib/libc/minimal/source/stdlib/atoi.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/libc/minimal/source/stdlib/atoi.c)

<a id="minimal-libc-bsd-string-and-conversion-files"></a>

## [最小C库（Minimal libc）的BSD字符串及转换文件](#id15)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

启用条件（Enabled by）：

[`CONFIG_MINIMAL_LIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MINIMAL_LIBC)

仅在选择最小C库（Minimal C Library）时编译进固件。

文件（Files，共5个）：


- [lib/libc/minimal/source/stdlib/strtol.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/libc/minimal/source/stdlib/strtol.c)
- [lib/libc/minimal/source/stdlib/strtoll.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/libc/minimal/source/stdlib/strtoll.c)
- [lib/libc/minimal/source/stdlib/strtoul.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/libc/minimal/source/stdlib/strtoul.c)
- [lib/libc/minimal/source/stdlib/strtoull.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/libc/minimal/source/stdlib/strtoull.c)
- [lib/libc/minimal/source/string/strstr.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/libc/minimal/source/string/strstr.c)

<a id="modern-cmake-sphinx-domain"></a>

## [Modern CMake的Sphinx域（Sphinx Domain）](#id16)

来源（Origin）：

[gitlab.kitware.com/cmake/cmake/-/tree/master/Utilities/Sphinx](https://gitlab.kitware.com/cmake/cmake/-/tree/master/Utilities/Sphinx)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

提供文档渲染所用的CMake域，不链接进固件。

文件（Files，共3个）：


- [doc/_extensions/moderncmakedomain/__init__.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_extensions/moderncmakedomain/__init__.py)
- [doc/_extensions/moderncmakedomain/cmake.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_extensions/moderncmakedomain/cmake.py)
- [doc/_extensions/moderncmakedomain/colors.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_extensions/moderncmakedomain/colors.py)

<a id="nouislider-library"></a>

## [noUiSlider库](#id17)

来源（Origin）：

[refreshless.com/nouislider](https://refreshless.com/nouislider/)

许可证（License）：

[MIT](https://spdx.org/licenses/MIT.html)

提供开发板目录中的Flash／RAM范围滑块，不链接进固件。

文件（Files，共2个）：


- [doc/_extensions/zephyr/domain/static/css/nouislider.min.css](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_extensions/zephyr/domain/static/css/nouislider.min.css)
- [doc/_extensions/zephyr/domain/static/js/nouislider.min.js](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_extensions/zephyr/domain/static/js/nouislider.min.js)

<a id="op-tee-message-interface-headers"></a>

## [开放可移植可信执行环境（OP-TEE）消息接口头文件](#id18)

来源（Origin）：

[www.op-tee.org](https://www.op-tee.org/)

许可证（License）：

[BSD-2-Clause](https://spdx.org/licenses/BSD-2-Clause.html)

启用条件（Enabled by）：

[`CONFIG_OPTEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPTEE)

仅在启用OP-TEE驱动时编译进固件。

文件（Files，共3个）：


- [drivers/tee/optee/optee_msg.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/tee/optee/optee_msg.h)
- [drivers/tee/optee/optee_rpc_cmd.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/tee/optee/optee_rpc_cmd.h)
- [drivers/tee/optee/optee_smc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/tee/optee/optee_smc.h)

<a id="openthread-spinel-hdlc-rcp-host-interface-files"></a>

## [OpenThread Spinel HDLC无线协处理器（RCP）主机接口文件](#id19)

来源（Origin）：

[openthread.io](https://openthread.io/)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

启用条件（Enabled by）：

[`CONFIG_HDLC_RCP_IF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HDLC_RCP_IF)

仅在启用Spinel HDLC RCP主机接口时链接进固件。

文件（Files，共3个）：


- [modules/openthread/platform/hdlc_interface.cpp](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/platform/hdlc_interface.cpp)
- [modules/openthread/platform/hdlc_interface.hpp](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/platform/hdlc_interface.hpp)
- [modules/openthread/platform/radio_spinel.cpp](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/platform/radio_spinel.cpp)

<a id="popper-js-library"></a>

## [Popper.js库](#id20)

来源（Origin）：

[popper.js.org](https://popper.js.org/)

许可证（License）：

[MIT](https://spdx.org/licenses/MIT.html)

由Tippy.js用于定位文档中的Doxygen悬浮提示（Tooltips），不链接进固件。

文件（Files，共1个）：


- [doc/_extensions/zephyr/doxytooltip/static/tippy/popper.min.js](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_extensions/zephyr/doxytooltip/static/tippy/popper.min.js)

<a id="posix-fnmatch-files"></a>

## [POSIX fnmatch文件](#id21)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

启用条件（Enabled by）：

[`CONFIG_POSIX_C_LIB_EXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_C_LIB_EXT)

仅在启用POSIX C库扩展时编译进固件。

文件（Files，共2个）：


- [include/zephyr/posix/fnmatch.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/posix/fnmatch.h)
- [subsys/portability/posix/c_lib_ext/fnmatch.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/c_lib_ext/fnmatch.c)

<a id="posix-sys-stat-h-header"></a>

## [POSIX sys/stat.h头文件](#id22)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

提供POSIX文件状态定义，在包含它的代码中编译进固件。

文件（Files，共1个）：


- [include/zephyr/posix/sys/stat.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/posix/sys/stat.h)

<a id="python-devicetree-library-files"></a>

## [Python设备树库（Devicetree Library）文件](#id23)

来源（Origin）：

[github.com/zephyrproject-rtos/python-devicetree](https://github.com/zephyrproject-rtos/python-devicetree)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

构建时用于解析设备树源文件，不链接进固件。

文件（Files，共8个）：


- [scripts/dts/gen_defines.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/gen_defines.py)
- [scripts/dts/python-devicetree/src/devicetree/_private.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/src/devicetree/_private.py)
- [scripts/dts/python-devicetree/src/devicetree/dtlib.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/src/devicetree/dtlib.py)
- [scripts/dts/python-devicetree/src/devicetree/edtlib.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/src/devicetree/edtlib.py)
- [scripts/dts/python-devicetree/tests/test-multidir.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-multidir.dts)
- [scripts/dts/python-devicetree/tests/test.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test.dts)
- [scripts/dts/python-devicetree/tests/test_dtlib.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test_dtlib.py)
- [scripts/dts/python-devicetree/tests/test_edtlib.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test_edtlib.py)

<a id="python-devicetree-library-test-files"></a>

## [Python设备树库（Devicetree Library）测试文件](#id24)

来源（Origin）：

[github.com/zephyrproject-rtos/python-devicetree](https://github.com/zephyrproject-rtos/python-devicetree)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

仅在测试python-devicetree库时使用，不链接进固件。

文件（Files，共104个）：


- [scripts/dts/python-devicetree/tests/test-bindings-2/multidir.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-2/multidir.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/allow-and-blocklist-child.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/allow-and-blocklist-child.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/allow-and-blocklist-multilevel.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/allow-and-blocklist-multilevel.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/allow-and-blocklist.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/allow-and-blocklist.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/allow-not-list.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/allow-not-list.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/allowlist.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/allowlist.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/block-not-list.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/block-not-list.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/blocklist.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/blocklist.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/class-bad-name.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/class-bad-name.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/class-base-1.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/class-base-1.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/class-base-2.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/class-base-2.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/class-child-base.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/class-child-base.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/class-child-union.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/class-child-union.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/class-dup.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/class-dup.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/class-union.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/class-union.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/empty-allowlist.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/empty-allowlist.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/empty-blocklist.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/empty-blocklist.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/filter-child-bindings.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/filter-child-bindings.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/include-2.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/include-2.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/include-invalid-keys.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/include-invalid-keys.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/include-invalid-type.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/include-invalid-type.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/include-no-list.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/include-no-list.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/include-no-name.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/include-no-name.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/include.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/include.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/intermixed.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/intermixed.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/simple.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/simple.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/simple_filter_allowlist.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/simple_filter_allowlist.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/simple_filter_blocklist.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/simple_filter_blocklist.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-include/simple_inherit.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-include/simple_inherit.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/base.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/base.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/base_amend.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/base_amend.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/base_inherit.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/base_inherit.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/base_multi.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/base_multi.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/compat_desc.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/compat_desc.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/compat_desc_base.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/compat_desc_base.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/compat_desc_multi.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/compat_desc_multi.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/default_base.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/default_base.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/default_override.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/default_override.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/default_override_include.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/default_override_include.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/default_required.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/default_required.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/diamond.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/diamond.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/filter_allows_notblocked.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/filter_allows_notblocked.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/filter_among_allowed.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/filter_among_allowed.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/filter_among_notblocked.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/filter_among_notblocked.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_child_propconst.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_child_propconst.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_child_propdefault.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_child_propdefault.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_child_propenum.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_child_propenum.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_child_propreq.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_child_propreq.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_child_proptype.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_child_proptype.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_grandchild_propconst.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_grandchild_propconst.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_grandchild_propdefault.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_grandchild_propdefault.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_grandchild_propenum.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_grandchild_propenum.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_grandchild_propreq.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_grandchild_propreq.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_grandchild_proptype.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_grandchild_proptype.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_propconst.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_propconst.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_propdefault.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_propdefault.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_propenum.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_propenum.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_propreq.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_propreq.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/invalid_proptype.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/invalid_proptype.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/simple.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/simple.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/simple_allowlist.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/simple_allowlist.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/simple_blocklist.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/simple_blocklist.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/simple_inherit.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/simple_inherit.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/thing.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/thing.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings-init/vnd,thing.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings-init/vnd,thing.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/bar-bus.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/bar-bus.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/child-binding-with-compat.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/child-binding-with-compat.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/child-binding.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/child-binding.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/child.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/child.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/defaults.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/defaults.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/dependency-mode.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/dependency-mode.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/deprecated.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/deprecated.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/device-on-any-bus.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/device-on-any-bus.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/device-on-bar-bus.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/device-on-bar-bus.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/device-on-foo-bus.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/device-on-foo-bus.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/enums.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/enums.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/false-positive.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/false-positive.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/foo-bus.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/foo-bus.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/foo-optional.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/foo-optional.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/foo-required.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/foo-required.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/gpio-dst.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/gpio-dst.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/gpio-src.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/gpio-src.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/grandchild-1.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/grandchild-1.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/grandchild-2.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/grandchild-2.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/grandchild-3.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/grandchild-3.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/interrupt-1-cell.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/interrupt-1-cell.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/interrupt-2-cell.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/interrupt-2-cell.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/interrupt-3-cell.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/interrupt-3-cell.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/min-max-len.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/min-max-len.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/min-max.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/min-max.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/multidir.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/multidir.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/order-1.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/order-1.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/order-2.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/order-2.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/parent.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/parent.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/phandle-array-controller-0.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/phandle-array-controller-0.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/phandle-array-controller-1.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/phandle-array-controller-1.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/phandle-array-controller-2.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/phandle-array-controller-2.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/props.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/props.yaml)
- [scripts/dts/python-devicetree/tests/test-bindings/test-cpu-fallback.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-bindings/test-cpu-fallback.yaml)
- [scripts/dts/python-devicetree/tests/test-wrong-bindings/wrong-address-cells-default.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-wrong-bindings/wrong-address-cells-default.yaml)
- [scripts/dts/python-devicetree/tests/test-wrong-bindings/wrong-phandle-array-name.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-wrong-bindings/wrong-phandle-array-name.yaml)
- [scripts/dts/python-devicetree/tests/test-wrong-bindings/wrong-size-cells-default.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-wrong-bindings/wrong-size-cells-default.yaml)
- [scripts/dts/python-devicetree/tests/test-wrong-bindings/wrong-specifier-space-type.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-wrong-bindings/wrong-specifier-space-type.yaml)
- [scripts/dts/python-devicetree/tests/test-wrong-bindings/wrong-status-default.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/dts/python-devicetree/tests/test-wrong-bindings/wrong-status-default.yaml)

<a id="risc-v-control-and-status-register-header"></a>

## [RISC-V控制与状态寄存器（CSR）头文件](#id25)

许可证（License）：

[SHL-0.51](https://spdx.org/licenses/SHL-0.51.html)

启用条件（Enabled by）：

[`CONFIG_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)

RISC-V控制与状态寄存器访问辅助代码，也可采用Apache-2.0许可；仅在RISC-V目标上编译进固件。

文件（Files，共1个）：


- [include/zephyr/arch/riscv/csr.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/arch/riscv/csr.h)

<a id="rv32m1-vega-board-openocd-configuration"></a>

## [RV32M1 VEGA开发板OpenOCD配置](#id26)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

OpenOCD在编程及调试rv32m1_vega开发板时使用，不链接进固件。

文件（Files，共2个）：


- [boards/openisa/rv32m1_vega/support/openocd_rv32m1_vega_ri5cy.cfg](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/openisa/rv32m1_vega/support/openocd_rv32m1_vega_ri5cy.cfg)
- [boards/openisa/rv32m1_vega/support/openocd_rv32m1_vega_zero_riscy.cfg](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/openisa/rv32m1_vega/support/openocd_rv32m1_vega_zero_riscy.cfg)

<a id="tf-m-secure-partition-sample-files"></a>

## [可信固件M（TF-M）安全分区示例文件](#id27)

来源（Origin）：

[www.trustedfirmware.org/projects/tf-m](https://www.trustedfirmware.org/projects/tf-m/)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

仅在构建TF-M安全分区集成示例时使用。

文件（Files，共2个）：


- [samples/tfm_integration/tfm_secure_partition/dummy_partition/tfm_dummy_partition.yaml.in](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_secure_partition/dummy_partition/tfm_dummy_partition.yaml.in)
- [samples/tfm_integration/tfm_secure_partition/dummy_partition/tfm_manifest_list.yaml.in](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_secure_partition/dummy_partition/tfm_manifest_list.yaml.in)

<a id="thread-metric-rtos-test-suite-source-files"></a>

## [Thread-Metric实时操作系统（RTOS）测试套件源文件](#id28)

来源（Origin）：

[github.com/eclipse-threadx/threadx](https://github.com/eclipse-threadx/threadx)

许可证（License）：

[MIT](https://spdx.org/licenses/MIT.html)

仅链接进Thread-Metric RTOS测试套件的测试固件。

文件（Files，共12个）：


- [tests/benchmarks/thread_metric/src/tm_api.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_api.h)
- [tests/benchmarks/thread_metric/src/tm_basic_processing_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_basic_processing_test.c)
- [tests/benchmarks/thread_metric/src/tm_cooperative_scheduling_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_cooperative_scheduling_test.c)
- [tests/benchmarks/thread_metric/src/tm_interrupt_preemption_processing_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_interrupt_preemption_processing_test.c)
- [tests/benchmarks/thread_metric/src/tm_interrupt_processing_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_interrupt_processing_test.c)
- [tests/benchmarks/thread_metric/src/tm_memory_allocation_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_memory_allocation_test.c)
- [tests/benchmarks/thread_metric/src/tm_message_processing_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_message_processing_test.c)
- [tests/benchmarks/thread_metric/src/tm_porting_layer.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_porting_layer.h)
- [tests/benchmarks/thread_metric/src/tm_porting_layer_zephyr.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_porting_layer_zephyr.c)
- [tests/benchmarks/thread_metric/src/tm_preemptive_scheduling_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_preemptive_scheduling_test.c)
- [tests/benchmarks/thread_metric/src/tm_synchronization_processing_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_synchronization_processing_test.c)
- [tests/benchmarks/thread_metric/thread_metric_readme.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/thread_metric_readme.txt)

<a id="tippy-js-library"></a>

## [Tippy.js库](#id29)

来源（Origin）：

[atomiks.github.io/tippyjs](https://atomiks.github.io/tippyjs/)

许可证（License）：

[MIT](https://spdx.org/licenses/MIT.html)

渲染文档Doxygen提示扩展中的悬浮提示，不链接进固件。

文件（Files，共1个）：


- [doc/_extensions/zephyr/doxytooltip/static/tippy/tippy-bundle.umd.min.js](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/_extensions/zephyr/doxytooltip/static/tippy/tippy-bundle.umd.min.js)

<a id="uf2-conversion-script"></a>

## [UF2转换脚本（Conversion Script）](#id30)

来源（Origin）：

[github.com/microsoft/uf2](https://github.com/microsoft/uf2)

许可证（License）：

[MIT](https://spdx.org/licenses/MIT.html)

构建时将固件镜像转换为UF2，不链接进固件。

文件（Files，共1个）：


- [scripts/build/uf2conv.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/build/uf2conv.py)

<a id="usb-device-stack-headers"></a>

## [USB设备协议栈头文件（USB Device Stack Headers）](#id31)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

启用条件（Enabled by）：

[`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)

属于旧USB设备协议栈，仅在启用该协议栈时编译进固件。

文件（Files，共2个）：


- [include/zephyr/usb/class/usb_dfu.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/usb_dfu.h)
- [include/zephyr/usb/usb_device.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/usb_device.h)

<a id="wireguard-vpn-files"></a>

## [WireGuard虚拟专用网络（VPN）文件](#id32)

来源（Origin）：

[github.com/smartalock/wireguard-lwip](https://github.com/smartalock/wireguard-lwip)

许可证（License）：

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)

启用条件（Enabled by）：

[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)

仅在启用WireGuard时编译进固件。

文件（Files，共7个）：


- [subsys/net/lib/wireguard/crypto/crypto.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/crypto/crypto.c)
- [subsys/net/lib/wireguard/crypto/crypto.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/crypto/crypto.h)
- [subsys/net/lib/wireguard/crypto/refc/blake2s.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/crypto/refc/blake2s.c)
- [subsys/net/lib/wireguard/crypto/refc/blake2s.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/crypto/refc/blake2s.h)
- [subsys/net/lib/wireguard/crypto/refc/hchacha20.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/crypto/refc/hchacha20.c)
- [subsys/net/lib/wireguard/crypto/refc/hchacha20.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/crypto/refc/hchacha20.h)
- [subsys/net/lib/wireguard/wg_crypto.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wireguard/wg_crypto.c)

<a id="xen-hypervisor-interface-files"></a>

## [Xen虚拟机监控器（Hypervisor）接口文件](#id33)

来源（Origin）：

[xenproject.org](https://xenproject.org/)

许可证（License）：

[MIT](https://spdx.org/licenses/MIT.html)

启用条件（Enabled by）：

[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)

仅在启用Xen客户机（Guest）支持时编译进固件。

文件（Files，共1个）：


- [drivers/xen/gnttab.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/xen/gnttab.c)

<a id="xoshiro128-prng"></a>

## [xoshiro128++伪随机数生成器（PRNG）](#id34)

来源（Origin）：

[prng.di.unimi.it](https://prng.di.unimi.it/)

许可证（License）：

[CC0-1.0](https://spdx.org/licenses/CC0-1.0.html)

启用条件（Enabled by）：

[`CONFIG_XOSHIRO_RANDOM_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XOSHIRO_RANDOM_GENERATOR)

仅在选择xoshiro128++伪随机数生成器（PRNG）时编译进固件。

文件（Files，共1个）：


- [subsys/random/random_xoshiro128.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/random_xoshiro128.c)

<a id="xtensa-startup-assembly-files"></a>

## [Xtensa启动汇编文件（Startup Assembly Files）](#id35)

许可证（License）：

[MIT](https://spdx.org/licenses/MIT.html)

启用条件（Enabled by）：

[`CONFIG_XTENSA_RESET_VECTOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_RESET_VECTOR)

仅在启用Xtensa复位向量（Reset Vector）时编译进固件。

文件（Files，共2个）：


- [arch/xtensa/core/startup/memctl_default.S](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/core/startup/memctl_default.S)
- [arch/xtensa/core/startup/memerror_vector.S](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/xtensa/core/startup/memerror_vector.S)

## 译注

本页说明官方Zephyr源码树中的组件许可例外。文件清单、SPDX许可标识及启用条件均对应原网页快照；源码路径是Zephyr仓库相对路径。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://coccinelle.gitlabpages.inria.fr/website/)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [](https://gcc.gnu.org/)：HTTP Error 403: Forbidden。
- [Sphinx](https://gitlab.kitware.com/cmake/cmake/-/tree/master/Utilities/Sphinx)：HTTP Error 403: Forbidden。

---

<!-- reading-navigation:start -->

**主线阅读**

[本模块主线目录](../reading/site_index.md) · [全部主线](../reading/README.md) · [下一篇：字母索引 A](P002_字母索引_A.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_字母索引_A.md)

</details>

<!-- reading-navigation:end -->
