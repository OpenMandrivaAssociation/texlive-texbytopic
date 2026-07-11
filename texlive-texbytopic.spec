%global tl_name texbytopic
%global tl_revision 68950

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Freed version of the book TeX by Topic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/texbytopic
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texbytopic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texbytopic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An invaluable book, originally published by Addison-Wesley (who have
released their copyright -- their version of the book went out of print
in the 1990s). The book describes itself as "a TeXnician's reference",
and covers the way TeX (the engine) works in as much detail as most
ordinary TeX programmers will ever need to know. A printed copy of the
book, slightly updated, may be had (for a modest price) from DANTE. The
original edition is available from Lulu. See the package home page for
details.

