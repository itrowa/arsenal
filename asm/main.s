	.file	"main.c"
	.text
	.globl	_bar
	.def	_bar;	.scl	2;	.type	32;	.endef
_bar:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$16, %esp
	movl	12(%ebp), %eax
	addl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	leave
	ret
	.globl	_foo
	.def	_foo;	.scl	2;	.type	32;	.endef
_foo:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$8, %esp
	movl	12(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	8(%ebp), %eax
	movl	%eax, (%esp)
	call	_bar
	leave
	ret
	.def	___main;	.scl	2;	.type	32;	.endef
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
	pushl	%ebp
	movl	%esp, %ebp
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$3, 4(%esp)
	movl	$2, (%esp)
	call	_foo
	movl	$0, %eax
	leave
	ret
