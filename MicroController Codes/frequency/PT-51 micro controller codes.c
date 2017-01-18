#include "at89c5131.h"
#include "stdio.h"

#define LCD_data  P2	    					// LCD Data port

void LCD_Init();

void LCD_DataWrite(char dat);
void LCD_CmdWrite(char cmd);
void LCD_StringWrite(char * str, unsigned char len);
void LCD_Ready();
void sdelay(int delay);
void delay_ms(int delay);

sbit LCD_rs = P0^0;  								// LCD Register Select
sbit LCD_rw = P0^1;  								// LCD Read/Write
sbit LCD_en = P0^2;  								// LCD Enable
sbit LCD_busy = P2^7;	


sbit T1=P3^4;

sbit VS=P1^4;
sbit VR=P1^5;
sbit VZ=P1^6;

sbit R0=P1^0;//10k
sbit R1=P1^1;//1M
sbit R2=P1^2;//100

int pulse;
int y;

//char a0[1],a1[1],a2[1],a3[1],a4[1],a5[1],a6[1];
//int y0,y1,y2,y3,y4,y5,y6;
char ascii[7];

void main()	{
	
				VS=1;
				VR=1;
				VZ=1;
	      R0=0;
	      R1=1;
				R2=1;
	
	

				P2 = 0x00;											// Make Port 2 output 
				P0 &= 0xF0;	


			  LCD_Init();
					
	
				T1=1 ; 
				TMOD = 0x15 ;
		   
							while(1)
											{   delay_ms(1000);
												
													TL0=0x00;
													TH0=0x00;
													TL1=0x80;
													TH1=0x3D;
												
													TR0=1;
													TR1=1;
													
													while(TF1==0){};
													
													TR0=0;
													TR1=0;
												  TF1=0;
													
												pulse=(TH0<<8)+TL0;
												y=pulse*40;
											 if(y>=1800 && y<=2200){
													VS=0;
													VR=1;
													VZ=1;	 
											 }	

											 if(y>=2300 && y<=2700){
													VS=1;
													VR=0;
													VZ=1;	 
											 }	

											 if(y>=2800 && y<=3300){
													VS=1;
													VR=1;
													VZ=0;	 
											 }												 
			


											 if(y>=3600 && y<=4300)
												 {R0=0;
												  R1=1;
													R2=1;
												 }
											 
									 		if(y>=4400 && y<=4800)
												 {R0=1;
												  R1=0;
													R2=1;
												 }		

											 if(y>=4900 && y<=5400)
												 {R0=1;
												  R1=1;
													R2=0;
												 }												 
											 									 
											 
											 
													

												sprintf(ascii,"%d",y);
												
										
									
												LCD_CmdWrite(0x80);
												LCD_StringWrite(ascii,7);
								
											}

										}
											
										
void LCD_Init()
{
  sdelay(100);
  LCD_CmdWrite(0x38);   	// LCD 2lines, 5*7 matrix
  LCD_CmdWrite(0x0E);			// Display ON cursor ON  Blinking off
  LCD_CmdWrite(0x01);			// Clear the LCD
  LCD_CmdWrite(0x80);			// Cursor to First line First Position
}



void LCD_CmdWrite(char cmd)
{
	LCD_Ready();
	LCD_data=cmd;     			// Send the command to LCD
	LCD_rs=0;         	 		// Select the Command Register by pulling LCD_rs LOW
  LCD_rw=0;          			// Select the Write Operation  by pulling RW LOW
  LCD_en=1;          			// Send a High-to-Low Pusle at Enable Pin
  sdelay(5);
  LCD_en=0;
	sdelay(5);
}


void LCD_DataWrite( char dat)
{
	LCD_Ready();
  LCD_data=dat;	   				// Send the data to LCD
  LCD_rs=1;	   						// Select the Data Register by pulling LCD_rs HIGH
  LCD_rw=0;    	     			// Select the Write Operation by pulling RW LOW
  LCD_en=1;	   						// Send a High-to-Low Pusle at Enable Pin
  sdelay(5);
  LCD_en=0;
	sdelay(5);
}



void LCD_StringWrite( char * str, unsigned char length)
{
    while(length>0)
    {
        LCD_DataWrite(*str);
        str++;
        length--;
    }
}


void LCD_Ready()
{
	LCD_data = 0xFF;
	LCD_rs = 0;
	LCD_rw = 1;
	LCD_en = 0;
	sdelay(5);
	LCD_en = 1;

	while(LCD_busy == 1)
	{
		LCD_en = 0;
		LCD_en = 1;
	}
	LCD_en = 0;
}



void sdelay(int delay)
{
	char d=0;
	while(delay>0)
	{
		for(d=0;d<5;d++);
		delay--;
	}
}


void delay_ms(int delay)
{
	int d=0;
	while(delay>0)
	{
		for(d=0;d<382;d++);
		delay--;
	}
}
