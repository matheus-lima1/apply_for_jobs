import React from 'react';
import { useRouter } from 'next/router';

export default function Home() {
  const router = useRouter();

  const handleExampleRoute = (e: any) => {
    router.push('/teste');
  };

  return (
    <div className="bg-black min-h-screen flex flex-col items-center justify-center space-y-6">
      <div
        className="w-3/4 h-1/4 bg-yellow-default rounded-lg flex items-center justify-center"
      >
        <span className="text-black text-xl font-bold">Opção 01</span>
      </div>
      <div
        className="w-3/4 h-1/4 bg-yellow-default rounded-lg flex items-center justify-center"
      >
        <span className="text-black text-xl font-bold">Opção 02</span>
      </div>
    </div>
  );
}
