{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca5d24a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "Первое задание:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "de940a57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3]\n",
      " [-2  3  0]\n",
      " [ 5  1  4]]\n",
      "[[ 1  2  3]\n",
      " [-2  4  6]\n",
      " [ 3  7  2]]\n",
      "[[-4]\n",
      " [ 1]\n",
      " [ 1]]\n",
      "[[ 3]\n",
      " [ 2]\n",
      " [10]]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import numpy as np\n",
    "\n",
    "A = np.array([[1, 2,3], [-2,3, 0],[5,1,4]])\n",
    "B = np.array([[1, 2,3], [-2,4, 6],[3,7,2]])\n",
    "u = np.array([[-4], [1],[1]])\n",
    "v = np.array([[3], [2],[10]])\n",
    "print (A)\n",
    "print (B)\n",
    "print (u)\n",
    "print (v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3a98e20",
   "metadata": {},
   "outputs": [],
   "source": [
    "Второе задание:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "5e3485f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.46581932 0.34147145 0.59781087 ... 0.96362259 0.71606726 0.53303579]\n",
      " [0.16073245 0.26715616 0.33801061 ... 0.3790876  0.98296378 0.80377101]\n",
      " [0.58864872 0.97318631 0.412194   ... 0.86426428 0.52460309 0.63028055]\n",
      " ...\n",
      " [0.48093004 0.29028934 0.50905926 ... 0.79344171 0.28997111 0.20897173]\n",
      " [0.49519556 0.05694362 0.5098278  ... 0.38514155 0.53475423 0.26359679]\n",
      " [0.62735544 0.4227712  0.02503144 ... 0.30074442 0.970153   0.2601268 ]]\n"
     ]
    }
   ],
   "source": [
    "C = np.random.random((100, 100))\n",
    "print (C)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "2b4400b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "w = np.random.random((100, 1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cb48bef",
   "metadata": {},
   "outputs": [],
   "source": [
    "Третье задание:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "9e9016d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 2  4  6]\n",
      " [-4  7  6]\n",
      " [ 8  8  6]]\n",
      "[[ 1  4  9]\n",
      " [ 4 12  0]\n",
      " [15  7  8]]\n",
      "[[  1   8  27]\n",
      " [ -8  27   0]\n",
      " [125   1  64]]\n",
      "[[ 1  8 27]\n",
      " [-8 36  0]\n",
      " [75  7 32]]\n"
     ]
    }
   ],
   "source": [
    "print(A+B)\n",
    "print(A*B)\n",
    "print(A*A*A)\n",
    "print(A*B*A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "d96273e1",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ -36   48 -600]\n",
      " [  18   18   30]\n",
      " [  27    0  120]]\n",
      "[[-12]\n",
      " [  2]\n",
      " [ 10]]\n",
      "[[0.13227546 0.09696526 0.16975617 ... 0.27363317 0.20333661 0.15136244]\n",
      " [0.01768389 0.0293927  0.03718816 ... 0.04170748 0.10814634 0.08843143]\n",
      " [0.41461005 0.68545605 0.29032557 ... 0.60873768 0.36950002 0.4439331 ]\n",
      " ...\n",
      " [0.00610269 0.00368358 0.00645963 ... 0.01006826 0.00367955 0.00265172]\n",
      " [0.26836299 0.03085965 0.27629269 ... 0.20872105 0.28980115 0.14285189]\n",
      " [0.03905185 0.02631681 0.00155817 ... 0.01872085 0.06039043 0.01619247]]\n",
      "[[0.13227546 0.03756892 0.42106334 ... 0.01222775 0.38806073 0.0331806 ]\n",
      " [0.04564207 0.0293927  0.23807509 ... 0.00481038 0.53270085 0.05003343]\n",
      " [0.16715446 0.10707062 0.29032557 ... 0.01096696 0.28429991 0.03923393]\n",
      " ...\n",
      " [0.13656634 0.03193783 0.35855185 ... 0.01006826 0.15714502 0.01300815]\n",
      " [0.14061722 0.00626498 0.35909316 ... 0.0048872  0.28980115 0.01640847]\n",
      " [0.17814574 0.04651358 0.0176307  ... 0.00381625 0.52575826 0.01619247]]\n"
     ]
    }
   ],
   "source": [
    "print(v.T*A.T*(u+2*u))\n",
    "print(u*v)\n",
    "print(C*w)\n",
    "print(w.T*C)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0975345",
   "metadata": {},
   "outputs": [],
   "source": [
    "Четвёртое задание:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "421ab15b",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = np.random.random((20, 20))\n",
    "number = 1\n",
    "for index in range(1,400):  \n",
    "    number *=index\n",
    "for i in range(20):\n",
    "    for j in range(20):\n",
    "        d[i,j] = i*j"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc546618",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
