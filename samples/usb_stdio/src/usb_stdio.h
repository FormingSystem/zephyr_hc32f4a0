/* Copyright The Zephyr HC32F4A0 Contributors
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef HC32_USB_STDIO_H_
#define HC32_USB_STDIO_H_

/* Application adapter: call once before using stdin, with Picolibc selected. */
int usb_stdio_init(void);

#endif /* HC32_USB_STDIO_H_ */
