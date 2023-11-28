---
title: "Communication protocol"
description: "SPI"
categories:
  - Coding
---

### Question

> SPI Driver
```

### Code [C]

```SPI

/*
* SPI_Config.h
*
* Created: 21/11/2023 8:45:13 PM
*  Author: Kirellos Emad Samir
*/


#ifndef SPI_CONFIG_H_
#define SPI_CONFIG_H_

#include "CPU_CONFIGURATION.h"

/************************************** SPI-Registers*************************************************/
/*
#define SPCR (*(volatile Uint8t* )(0x2D))
#define SPSR (*(volatile Uint8t* )(0x2E))
#define SPDR (*(volatile Uint8t* )(0x2F))
*/

#define MASTER 0
#define SLAVE  1

#define SPI_MODE MASTER

#define MOSI 5
#define MISO 6
#define SCK  7
#define SS   4




#endif /* SPI_CONFIG_H_ */



/*
* SPI.h
*
* Created: 21/11/2023 8:00:16 PM
*  Author: Kirellos Emad Samir
*/


#ifndef SPI_H_
#define SPI_H_

#include "SPI_CONFIG.h"

void SPI_INIT(void);
void SPI_TRANSMIT(Uint8t data);
void SPI_RECEIVE(Uint8t* data);
void SPI_SLAVESELECT(Uint8t slave);

#endif /* SPI_H_ */

/*
* SPI.c
*
* Created: 21/11/2023 8:29:11 PM
*  Author: Kirellos Emad Samir
*/

#include "SPI.h"

void SPI_INIT(void)
{
	#if SPI_MODE == MASTER
	/*Define directions for Master pins*/
	SET_BIT(DDRB, MOSI);                                          /*MOSI-OUTPUT*/
	CLR_BIT(DDRB, MISO);                                           /*MISO-INPUT*/
	SET_BIT(DDRB, SCK);                                         /*CLK-OUTPUT*/
	SET_BIT(DDRB, SS);
	CLR_BIT(SPCR, SPIE);                                          /*Disable SPI Interrupt*/
	SET_BIT(SPCR, MSTR);                                          /*Select Master Mode*/
	SET_BIT(SPCR, DORD);                                          /*Data order mode-LSB First*/
	CLR_BIT(SPCR, CPOL);                                          /*Clock Phase-LOW*/
	CLR_BIT(SPSR, SPI2X);SET_BIT(SPCR, SPR1);SET_BIT(SPCR, SPR0); /*Prescaler-128*/
	SET_BIT(SPCR, SPE);                                             /*SS-OUTPUT*/
	#elif SPI_MODE == SLAVE
	/*Define directions for Slave pins*/
	CLR_BIT(DDRB, MOSI);                                          /*MOSI-INPUT*/
	SET_BIT(DDRB, MISO);                                           /*MISO-OUTPUT*/
	CLR_BIT(DDRB, SCK);                                            /*CLK-INPUT*/
	CLR_BIT(DDRB, SS);
	CLR_BIT(SPCR, MSTR);
	SET_BIT(SPCR, SPE);                                           /*Enable SPI*/                                         /*SS-INPUT*/
	#endif
}
void SPI_TRANSMIT(Uint8t data)
{
	SPDR = data;
	while (GET_BIT(SPSR, SPIF) != 1);
}
void SPI_RECEIVE(Uint8t* data)
{
	while (GET_BIT(SPSR, SPIF) != 1);
	*data = SPDR;
}
void SPI_SLAVESELECT(Uint8t slave)
{
	if(slave == 0)
	{
		CLR_BIT(PORTB, SS);
	}
}

```

> Time Complexity = O(N)

> Space Complexity = O(1)
